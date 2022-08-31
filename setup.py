from distutils.core import setup, Extension


def main():
    setup(name="extend",
        version="1.0.0",
        description="extend test",
        author="Brendon",
        ext_modules=[Extension("extend", ["extend.c"])])

if __name__=="__main__":
    main()
