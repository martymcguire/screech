#!/usr/bin/env python

def main():
    from screech.app import create_app
    app = create_app()
    app.run(debug=True, port=5000)

main()
