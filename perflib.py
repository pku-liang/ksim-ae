from pathlib import Path
import subprocess
import json

perf_events = [
  # "cache-references",
  # "cache-misses",
  # "stalled-cycles-frontend",
  # "stalled-cycles-backend",
  # "L1-dcache-load-misses",
  # "L1-dcache-loads",
  # "L1-dcache-prefetches",
  # "L1-icache-load-misses",
  # "L1-icache-loads",
  # "l1_data_cache_fills_all",
  "all_data_cache_accesses",
  # "l2_cache_hits_from_dc_misses",
  # "l2_cache_misses_from_dc_misses",
  # "l2_cache_hits_from_ic_misses",
  # "l2_cache_misses_from_ic_miss",
  # "sse_avx_stalls",
  # "task-clock",
  # "cache-misses",
  "cycles",
  "instructions",
  # "branches",
  # "branch-misses",
]

def check_events():
  result = subprocess.run(["perf", "list"], capture_output=True, shell=True)
  for event in list(perf_events):
    if event not in result.stdout:
      print(f'remove unsupported perf event: {event}')
      perf_events.remove(event)
  print('perf event: ', ' '.join(perf_events))

check_events()

perf_groups = [
  # 'l2_cache'
]

def make_perf_command():
  perf_commands = ['perf', 'stat', '-j']
  if perf_events: perf_commands += ['-e', ','.join(perf_events)]
  if perf_groups: perf_commands += ['-M', ','.join(perf_groups)]
  perf_commands = ' '.join(perf_commands)
  return perf_commands

perf_command = make_perf_command()

def parse_perf(perf: str):
  fields = {}
  for line in perf.split('\n'):
    if not line.strip(): continue
    field = json.loads(line)
    if 'event' in field:
      value = field['counter-value']
      name = field['event'].replace(':u', '')
      if value == '<not counted>':
        print(f'{name} is not counted')
        return None
    else:
      value = field['metric-value']
      name = field['metric-unit']
      name = name.replace('%  ', '').replace(':u', '')
      if value == '<not counted>':
        print(f'{name} is not counted')
        return None
    fields[name] = value
  return fields

def run_task(bench:str, sim:str, exe: Path, taskset:str, results_dir: Path, num_runs: int, run_cycle: int):
  if not exe.exists():
    print(f'{exe} not found')
    return
  res = results_dir.joinpath(f'{bench}-{sim}.json')
  if res.exists() and exe.stat().st_mtime < res.stat().st_mtime:
    print(f'nothing to do for {res}')
    return
  cur_run_cycle = run_cycle
  run_data = []
  for run in range(num_runs):
    rerun = True
    while rerun:
      rerun = False
      run_field = {
        'simulator': sim,
        'benchmark': bench,
        'sim-cycles': cur_run_cycle,
        'run': run
      }
      print(run_field)
      cmd_line = f'{taskset} {perf_command} {exe} {cur_run_cycle}'
      proc = subprocess.Popen(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
      stdout, stderr = proc.communicate()
      perf = stderr.decode()
      try:
        tm = int(stdout.decode())
      except:
        print('ERROR: ', cmd_line)
        print(perf)
        exit(1)
      run_field['time'] = tm
      perf = parse_perf(perf)
      if perf is None:
        rerun = True
        cur_run_cycle *= 2
      else:
        run_field.update(perf)
        run_data.append(run_field)
  with res.open('w') as f:
    f.write(json.dumps(run_data, indent=2))
