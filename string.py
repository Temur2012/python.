# capitalize
print("hello".capitalize())
print("python".capitalize())

# casefold
print("HELLO".casefold())
print("PyThOn".casefold())

# center
print("hi".center(10))
print("hi".center(10, "-"))

# count
print("banana".count("a"))
print("hello".count("l"))

# encode
print("hello".encode())
print("salom".encode("utf-8"))

# endswith
print("file.py".endswith("py"))
print("test.txt".endswith(".jpg"))

# expandtabs
print("a\tb".expandtabs(4))
print("1\t2\t3".expandtabs(2))

# find
print("hello".find("e"))
print("hello".find("x"))

# format
print("My name is {}".format("Ali"))
print("{} + {} = {}".format(2, 3, 5))

# format_map
print("Hello {name}".format_map({"name": "Ali"}))
print("Age: {age}".format_map({"age": 20}))

# index
print("hello".index("e"))
print("banana".index("n"))

# isalnum
print("abc123".isalnum())
print("abc 123".isalnum())

# isalpha
print("hello".isalpha())
print("hello1".isalpha())

# isascii
print("hello".isascii())
print("ñ".isascii())

# isdecimal
print("123".isdecimal())
print("12.3".isdecimal())

# isdigit
print("123".isdigit())
print("²".isdigit())

# isidentifier
print("var1".isidentifier())
print("1var".isidentifier())

# islower
print("hello".islower())
print("Hello".islower())

# isnumeric
print("123".isnumeric())
print("½".isnumeric())

# isprintable
print("hello".isprintable())
print("hello\n".isprintable())

# isspace
print("   ".isspace())
print(" a ".isspace())

# istitle
print("Hello World".istitle())
print("hello world".istitle())

# isupper
print("HELLO".isupper())
print("Hello".isupper())

# join
print(",".join(["a", "b", "c"]))
print(" ".join(["Hello", "World"]))

# ljust
print("hi".ljust(5))
print("hi".ljust(5, "*"))

# lower
print("HELLO".lower())
print("PyThOn".lower())

# lstrip
print("  hi".lstrip())
print("***hi".lstrip("*"))

# maketrans / translate
t = str.maketrans("a", "x")
print("apple".translate(t))
t2 = str.maketrans("abc", "123")
print("abc".translate(t2))

# partition
print("hello-world".partition("-"))
print("user@mail.com".partition("@"))

# replace
print("hello".replace("l", "x"))
print("banana".replace("a", "o"))

# rfind
print("banana".rfind("a"))
print("hello".rfind("l"))

# rindex
print("banana".rindex("a"))
print("hello".rindex("l"))

# rjust
print("hi".rjust(5))
print("hi".rjust(5, "0"))

# rpartition
print("a=b=c".rpartition("="))
print("hello-world".rpartition("-"))

# rsplit
print("a,b,c".rsplit(","))
print("a,b,c".rsplit(",", 1))

# rstrip
print("hi   ".rstrip())
print("hi***".rstrip("*"))

# split
print("a,b,c".split(","))
print("hello world".split())

# splitlines
print("a\nb\nc".splitlines())
print("a\nb".splitlines(True))

# startswith
print("hello".startswith("he"))
print("hello".startswith("Hi"))

# strip
print("  hi  ".strip())
print("***hi***".strip("*"))

# swapcase
print("Hello".swapcase())
print("PyThOn".swapcase())

# title
print("hello world".title())
print("python programming".title())

# upper
print("hello".upper())
print("python".upper())

# zfill
print("7".zfill(3))
print("123".zfill(5))
