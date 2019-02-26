inotifywait -m /home/hello/here -e create -e moved_to |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        echo "executing $SCRIPT_PATH"
        python3 $SCRIPT_PATH
    done
