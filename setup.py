from distutils.core import setup, Extension

def main():
    setup(name="rps",
        version="1.0.0",
        description="rps test",
        author="Brendon",
        ext_modules=[Extension("rps", ["rps.c"])])

if __name__=="__main__":
    main()

