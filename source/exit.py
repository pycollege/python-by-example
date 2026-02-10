import sys

# Exit with error code for certain conditions
if "--fail" in sys.argv:
    print("Exiting with error")
    sys.exit(1)

# Normal end of script
print("Program completed")
sys.exit(0)
