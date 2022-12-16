#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size
curl -s -I "$1" | grep "Content-Length: " | cut  -b 17-
