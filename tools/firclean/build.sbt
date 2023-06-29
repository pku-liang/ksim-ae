organization := "kk.keke"

version := "0.8-SNAPSHOT"

name := "firclean"

scalaVersion := "2.12.13"

scalacOptions ++= Seq("-deprecation", "-unchecked")

libraryDependencies += "edu.berkeley.cs" %% "firrtl" % "1.5.1"

assemblyJarName in assembly := "firclean.jar"

assemblyOutputPath in assembly := file("./firclean.jar")
