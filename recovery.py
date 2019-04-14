# Recover data after running "git reset --hard origin/master" by mistake
# 1) Saving all the hashed into a file first
# "git fsck --cache --unreachable $(git for-each-ref --format="%(objectname)") > allhashes"
# 2) See contents of each file by using "git show"
# Here, all hashed are put in a list. Recover each file automatic.
# Ref: https://stackoverflow.com/questions/7374069/undo-git-reset-hard-with-uncommitted-files
# -in-the-staging-area/20997627

commits = ["49569ae09b32450dbf8aadf5989c2d1d30ca17d6",
           "59ef096e19c8ee8dfd79083d8a3f68eb8211341f",
           "a3cc057b45a75170627d1a82fedbc392112f010f",
           "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
           "697f7f0b742107aa41dc201d3f823f6ca4a29f81",
           "2a941f3f75380a62c3276129f396a07a3b506a53",
           "741b39661dc620058d5cd57dfafdbe3694e8d1ea",
           "355bde93458f27a8c6f5ecd876bf3a88d4b92c55",
           "37fbbfad76dabb507a231d9a14e7f919b076234b",
           "39613337dcab10151f33256fdeed07bc5db6fd5e",
           "bbb4e266ae582d0494899a75e12e7cd1a379a841",
           "b6960db7fe487bd60e7e655cd05ed2ef132291b2",
]
from subprocess import call
filename = "file"
i = 1
for c in commits:
    f = open(filename + str(i), "wb")
    call(["git", "show", c], stdout=f)
    i += 1

