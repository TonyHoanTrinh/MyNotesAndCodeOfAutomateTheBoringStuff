# Assertions force conditions to be true, other they end the program and print an error message

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'notopen'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
