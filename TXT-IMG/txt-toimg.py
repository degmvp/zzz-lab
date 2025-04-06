from PIL import Image, ImageDraw, ImageFont

# Função para criar uma imagem a partir de um arquivo .txt
def txt_to_image(txt_file, output_image):
    # Lê o conteúdo do arquivo .txt
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Configurações da imagem
    font_size = 20  # Tamanho da fonte
    font = ImageFont.truetype("arial.ttf", font_size)  # Fonte (use uma fonte disponível no seu sistema)
    padding = 20  # Espaçamento nas bordas
    line_height = font_size + 5  # Altura entre as linhas

    # Calcula as dimensões da imagem com base no texto
    lines = text.split('\n')
    max_line_width = max(font.getlength(line) for line in lines)
    image_width = int(max_line_width) + 2 * padding
    image_height = len(lines) * line_height + 2 * padding

    # Cria a imagem
    image = Image.new("RGB", (image_width, image_height), color="white")
    draw = ImageDraw.Draw(image)

    # Desenha o texto na imagem
    y = padding
    for line in lines:
        draw.text((padding, y), line, font=font, fill="black")
        y += line_height

    # Salva a imagem
    image.save(output_image)
    print(f"Imagem gerada: {output_image}")

# Exemplo de uso
txt_to_image("code-node.txt", "saida.jpg")
