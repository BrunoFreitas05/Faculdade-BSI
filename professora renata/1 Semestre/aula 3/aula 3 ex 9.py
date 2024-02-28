t=float(input("Digite a nota do Trabalho: "))
a=float(input("Digite a nota da Avaliação: "))
e=float(input("Digite a nota do Exame: "))
media=(t*2+a*3+e*5)/10
if media<3:
    print(f"Reprovado com media {media}")
elif media<5:
    print(f"Recuperação com media {media}")
else:
    print(f"Aprovado com media {media}").


