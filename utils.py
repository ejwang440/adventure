from termcolor import colored

def choices_to_str(choices):
  prompt = "["
  for choice in choices:
    prompt += colored(choice, attrs=[]) + ", "
  prompt = prompt[:-2]
  prompt += "]"
  return prompt