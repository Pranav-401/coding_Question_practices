try:
    def move_hashes_to_front(data):
        hashes = ''
        other = ''
        for char in data:
            if char == "#":
                hashes += '#'
            else:
                other += char
        return hashes + other

    print(move_hashes_to_front("#h#i#"))

except Exception as e:
    print(f"Error: {e}")
