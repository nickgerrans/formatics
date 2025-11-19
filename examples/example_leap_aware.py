# ORIGIN:/home/user/formatics

# This script is now leap-aware!
# When you move it to a different directory, filestate will:
# 1. Detect the move
# 2. Print the old and new locations
# 3. Run this script once automatically
# 4. Update the ORIGIN tag in this file

print("Hello from a leap-aware script!")
print(f"I'm located at: {__file__}")
