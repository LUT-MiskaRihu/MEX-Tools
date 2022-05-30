# KuunteluApuri

print("Tämä työkalu generoi XML-koodin rajoitettua kuuntelua varten.")
print()
print()

while (True):
    print("Anna liitetiedoston nimi tiedostopäätteen kanssa.")
    print("Esim. 'kuuntelu1.mp3'")
    src = input("src: ")

    print()
    print("Anna äänitteen otsikko.")
    print("Esim. 'The whole recording'")
    print("Esim. 'The passage related to question 1.1.'")
    title = input("title: ")

    print()
    print("Anna toistokertojen max lukumäärä kokonaislukuna.")
    times = input("times: ")

    print()
    print()
    print("XML-koodi:")
    print()
    print(80 * "-")
    code = ""
    code += "<e:audio src=\"{src}\" times=\"{times}\">\n"
    code += "\t<e:audio-title>{title}</e:audio-title>\n"
    code += "<e:audio>"
    print(code.format(src=src, title=title, times=times))
    print(80 * "-")
    print()
    print()
