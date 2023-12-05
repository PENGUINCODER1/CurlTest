from os import scandir, system
from time import sleep

frame = 1
max_frame = 10
while True:
  if frame == max_frame + 1:
    frame = 1
  f = open(f"frames/{frame}")
  print(f.read())
  frame = frame + 1
  sleep(0.1)
  system("clear")
