from os import scandir, system
from time import sleep

frame = 1
max_frame = 3
while True:
  if frame == max_frame + 1:
    frame = 1
  frameString = system(F"curl https://penguincoder1.github.io/CurlTest/frames/{frame}")
  print(frameString)
  frame = frame + 1
  sleep(0.1)
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
