import os
from PIL import Image

def concatenar_imagens(pasta_imagens, arquivo_saida="questoes_concat.png", espacamento=20):
    # Obter lista de arquivos de imagem na pasta 'recortadas'
    caminho_pasta = pasta_imagens
    arquivos = [f for f in os.listdir(caminho_pasta) 
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    # Ordenar os arquivos para manter a sequência correta
    arquivos.sort()
    
    if not arquivos:
        print("Nenhuma imagem encontrada na pasta 'recortadas'!")
        print("Verifique se:")
        print("1. A pasta 'recortadas' existe no mesmo local do script")
        print("2. As imagens estão nos formatos: PNG, JPG, JPEG, BMP ou GIF")
        return
    
    print(f"Encontradas {len(arquivos)} imagens na pasta 'recortadas'")
    print("Imagens encontradas:", arquivos)
    
    # Carregar as imagens
    imagens = []
    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        img = Image.open(caminho_completo)
        imagens.append(img)
        print(f"Carregada: {arquivo} ({img.width}x{img.height})")
    
    # Calcular dimensões da imagem final
    largura_max = max(img.width for img in imagens)
    altura_total = sum(img.height for img in imagens) + (espacamento * (len(imagens) - 1))
    
    # Criar imagem em branco
    imagem_final = Image.new('RGB', (largura_max, altura_total), color='white')
    
    # Colar cada imagem uma embaixo da outra
    y_offset = 0
    for i, img in enumerate(imagens):
        # Centralizar horizontalmente se for mais estreita que a largura máxima
        x_offset = (largura_max - img.width) // 2
        imagem_final.paste(img, (x_offset, y_offset))
        y_offset += img.height + espacamento
        print(f"Adicionada questão {i+1}: {arquivos[i]}")
    
    # Salvar imagem resultante
    imagem_final.save(arquivo_saida)
    print(f"\n✅ Imagem concatenada salva como '{arquivo_saida}'")
    print(f"📊 Dimensões finais: {largura_max}x{altura_total} pixels")
    print(f"📋 Total de questões processadas: {len(imagens)}")

# Configurações - AGORA USANDO A PASTA "recortadas"
pasta_com_imagens = "recortadas"  # Nome corrigido para sua pasta
nome_arquivo_saida = "todas_questoes_enem.png"

# Executar
concatenar_imagens(pasta_com_imagens, nome_arquivo_saida)