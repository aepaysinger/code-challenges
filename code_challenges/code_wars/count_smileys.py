def count_smileys(smiley_faces):
    parts_of_face = {"eyes": [":", ";"], "nose": ["-", "~"], "mouth": ["D", ")"]}
    count = 0
    for face in smiley_faces:
        if len(face) == 2:
            if face[0] in parts_of_face["eyes"]:
                if face[-1] in parts_of_face["mouth"]:
                    count += 1
        if len(face) == 3:
            if face[0] in parts_of_face["eyes"]:
                if face[-1] in parts_of_face["mouth"]:
                    if face[1] in parts_of_face["nose"]:
                        count += 1

    return count


if __name__ == "__main__":
    smiley_faces = [":D", ":~)", ";~D", ":)"]
    print(count_smileys(smiley_faces))
