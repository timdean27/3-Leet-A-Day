# Problem Statement: Version Comparison
# Software versions are stored as a string with up to five parts, formatted as [major].[minor].[patch].[build].[compilation]. 
# Each part of the version is always a non-negative integer. 
# Versions may be of varying lengths, such as "2", "1.5", or "2.12.4.0.6". 
# The period (.) is used solely as a separator and does not represent a decimal point.

# You need to write an algorithm that takes two version strings as input parameters: version1 and version2. 
# The algorithm should compare the two versions and return:

# -1 if version1 is less than version2
# 0 if version1 is equal to version2
# 1 if version1 is greater than version2
# You can assume all inputs are valid, and each version part will be a non-negative integer less than 100.

# Examples:
# "2" == "2.0" == "2.0.0" == "2.0.0.0.0" should return 0 in each case.
# "2" < "2.0.0.0.1" should return -1.
# "2" < "2.1" should return -1.
# "2.1.0" > "2.0.1" should return 1.

def version_compare( version1, version2 ) :
	# split the version by '.' this is a dilimiter 
    # creat arrays to compair indiviual pieces
    v1_pieces= [int(piece) for piece in version1.split('.')]
    v2_pieces= [int(piece) for piece in version2.split('.')]

    print("v1_pieces",v1_pieces,"v2_pieces",v2_pieces)

    # we want to run a for loop to compare the parts individualy 
    # example 2.1.0 and 2.0.1 we get 1 so version 1 is greater we can determine this at the second value
    # but arrays v1_pieces and v2_pieces must be equal length for cases like 2 and 2.0.0.0 being eqaul

    max_length = max(len(v1_pieces) , len(v2_pieces))
    # add zeros for diffrence in length
    v1_pieces.extend([0] * (max_length - len(v1_pieces)))
    v2_pieces.extend([0] * (max_length - len(v2_pieces)))


    # run loop to compare each part 
    # exit then v1_pieces[i] is less than v2_pieces[i] with -1
    # exit then v1_pieces[i] is greater than v2_pieces[i] with -1

    for i in range(max_length):
        if v1_pieces[i] < v2_pieces[i]:
            # means version 1 is less than version 2
            return -1
        if v1_pieces[i] > v2_pieces[i]:
            # means version 1 is greater than version 2
            return 1
    # if equal we pass through loop and retun 0
    return 0

print(version_compare("2.0.0","2.0.0.0.0")) # values are equal return 0
print(version_compare("2.0.0","2.0.0.0.1")) # version 2 is greater retun -1
print(version_compare("2.0.0.1","2.0.0.0.1")) #version 1 is greater retun 1