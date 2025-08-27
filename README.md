Network Ping Logger

This Python script checks whether one or more hosts (DNS names or IP addresses) are reachable via ping and logs the results to a text file.

Features:
Allows the user to enter multiple hosts at once, separated by spaces.
Detects whether each host is a Private IP or Public IP.
Checks if each host is ONLINE or OFFLINE using a single ping.
Logs all results into a single text file (hosts_status.txt) without overwriting previous entries.
Prints the status of each host in the console in real time.

How it works:
The script asks the user for host(s) to check.
It detects the OS type (Windows or Linux/Mac) to use the correct ping parameter.
For each host, it:
Sends a single ping request.
Determines if the host is private or public based on IP address prefixes (192., 10., 172.).
Prints the host’s status (ONLINE or OFFLINE) to the console.
Appends the host, IP type, and status to hosts_status.txt.
If the text file doesn’t exist, it creates it and adds a header.
New results are always appended, so previous entries remain in the file.
