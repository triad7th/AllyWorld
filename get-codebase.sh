# Find all visible .json and .swift files recursively
echo "I'm going to show the current codebase. ANSWER future questions based on this codebase."
echo "@@@CODEBASE START@@@"

find . -type f \( -name "*.html" -o -name "*.sh" \) ! -path "*/.*/*" ! -name ".*" | while read -r filepath; do
    echo "* File Relative Path"
    echo "* -----------------"
    echo "* $filepath"
    echo ""
    cat "$filepath"
    echo ""
    echo "-----------------------------"
    echo ß""
done

echo "@@@CODEBASE END@@@"
