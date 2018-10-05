def main():
    while True:
        try:
            a = input("""
1=build      Build the MkDocs documentation
2=gh-deploy  Deploy your documentation to GitHub Pages
3=serve      Run the builtin development server
4=sair
=>""")
            if a  == "1":
                from os import system
                system("mkdocs  build --verbose")
            elif a =="2":
                from os import system
                system ( "mkdocs  gh-deploy --verbose" )
            elif a == "3":
                from os import system
                system ( "mkdocs  serve --verbose" )
            elif a == "4":
                exit(1)
            else:
                pass
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass

if __name__ == '__main__':
    main()