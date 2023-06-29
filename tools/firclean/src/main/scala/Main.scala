
import firrtl._
import firrtl.ir._
import scala.collection.mutable
import scala.io.Source
import java.io.File
import java.io.PrintWriter

object Main extends App {
  private def writeFile(path: File, content: String): Unit =
    Some(new PrintWriter(path)).foreach{ p =>
      try { p.write(content) } finally { p.close() }
    }

  private def removeAssertion(c: Circuit): Circuit = {
    def onStmt(s: Statement): Statement =
      s mapStmt onStmt match {
        case _: Print => EmptyStmt
        case _: Verification => EmptyStmt
        case o => o
      }
    c.mapModule(_.mapStmt(onStmt))
  }
  private def removePlusarg(c: Circuit): Circuit = {
    val modMap = c.modules.map(_.name).zip(c.modules).toMap
    def onModule(d: DefModule): DefModule = {
      val delSet = mutable.Set[String]()
      def removeInst(s: Statement): Statement = s mapStmt removeInst match {
        case d@DefInstance(_, name, module, _) =>
          modMap(module) match {
            case ExtModule(_, _, _, defname, _) =>
              defname match {
                case "plusarg_reader" =>
                  delSet += name
                  EmptyStmt
                case _ => d
              }
            case _ => d
          }
        case o => o
      }
      def removeConnE(e: Expression): Expression = e mapExpr removeConnE match {
        case SubField(Reference(name, _, _, _), fieldName, tpe, flow)
          if delSet contains name =>
          UIntLiteral(BigInt(0))
        case o => o
      }
      def removeConnS(s: Statement): Statement = s mapStmt removeConnS mapExpr removeConnE
      d mapStmt removeInst mapStmt removeConnS
    }
    c mapModule onModule
  }

  private val src = Source.fromFile(args(0))
  private var circuit = Parser.parse(src.getLines())
  circuit = removeAssertion(circuit)
  circuit = removePlusarg(circuit)
  writeFile(new File(args(1)), circuit.serialize)
}