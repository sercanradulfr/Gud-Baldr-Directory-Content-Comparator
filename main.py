import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Gud Baldr")
print(ascii_banner)

def calculate_file_hash(filename):
    """
    Calculates the hash value of a file using the SHA256 algorithm.
    """
    try:
        with open(filename, "rb") as file:
            file_content = file.read()
            file_hash = hashlib.sha256(file_content).hexdigest()
            return file_hash
    except IOError:
        print("Error: File not found or inaccessible.")
        return None

def scan_directory(directory):
    """
    Scans a directory and calculates the hash value of each file within it.
    """
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash:
                file_hashes[file_path] = file_hash
    return file_hashes

def compare_directories(dir1, dir2):
    """
    Compares the contents of two directories by calculating and comparing the file hashes.
    """
    dir1_hashes = scan_directory(dir1)
    dir2_hashes = scan_directory(dir2)

    common_files = set(dir1_hashes.keys()).intersection(set(dir2_hashes.keys()))

    changed_files = []
    added_files = []
    deleted_files = []

    for file_path in common_files:
        if dir1_hashes[file_path] != dir2_hashes[file_path]:
            changed_files.append(file_path)

    for file_path in set(dir1_hashes.keys()) - set(dir2_hashes.keys()):
        deleted_files.append(file_path)

    for file_path in set(dir2_hashes.keys()) - set(dir1_hashes.keys()):
        added_files.append(file_path)

    return {
        "changed_files": changed_files,
        "added_files": added_files,
        "deleted_files": deleted_files
    }

# Example usage
dir1 = "/path/to/directory1"
dir2 = "/path/to/directory2"

result = compare_directories(dir1, dir2)

print("Changed files:")
for file_path in result["changed_files"]:
    print(file_path)

print("Added files:")
for file_path in result["added_files"]:
    print(file_path)

print("Deleted files:")
for file_path in result["deleted_files"]:
    print(file_path)
