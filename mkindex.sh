#!/bin/bash

# Caminho do diretório raiz
root_dir="."

# Função para gerar o arquivo index.html
generate_index() {
    local dir="$1"
    local index_file="$dir/index.html"

    echo "Gerando $index_file"
    
    # Cabeçalho do arquivo HTML
    echo "<!DOCTYPE html>" > "$index_file"
    echo "<html lang=\"pt-BR\">" >> "$index_file"
    echo "<head>" >> "$index_file"
    echo "    <meta charset=\"UTF-8\">" >> "$index_file"
    echo "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">" >> "$index_file"
    echo "    <title>Vicente V. Figueira</title>" >> "$index_file"
    echo "    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        header {
            background: #cc0000;
            color: #fff;
            padding: 1.5rem 0;
            text-align: center;
        }
        nav {
            background: #333;
            color: #fff;
            padding: 0.5rem 0;
            text-align: center;
        }
        nav a {
            color: #fff;
            margin: 0 1rem;
            text-decoration: none;
        }
        nav a:hover {
            text-decoration: underline;
        }
        main {
            padding: 1rem;
            max-width: 800px;
            margin: 0 auto;
        }
        .section {
            margin-bottom: 2rem;
        }
        .section h2 {
            color: #cc0000;
            border-bottom: 2px solid #cc0000;
            padding-bottom: 0.5rem;
        }
        .section ul {
            list-style: none;
            padding: 0;
        }
        .section ul li {
            background: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-bottom: 0.5rem;
            padding: 1rem;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        footer {
            text-align: center;
            padding: 1rem 0;
            background: #cc0000;
            color: #fff;
            margin-top: 2rem;
        }
        .contact-info {
            background: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 1rem;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }
        .contact-info h2 {
            color: #cc0000;
            margin-top: 0;
        }
    </style>" >> "$index_file"
    echo "</head>" >> "$index_file"
    echo "<body>" >> "$index_file"
    echo "<header>
        <h1>Vicente Viater Figueira</h1>
        <p>Aluno de Mestrado no Instituto de Física da Universidade de São Paulo</p>
    </header>

    <nav>
        <a href=\"#notas\">Notas de Física</a>
        <a href=\"#exercicios\">Exercícios</a>
        <a href=\"#solucoes\">Soluções de Exercícios</a>
        <a href=\"#informacoes\">Informações Pessoais</a>
    </nav>" >> "$index_file"
    echo "    <main><section class=\"section\"><h1>Index of $(basename "$dir")</h1>" >> "$index_file"
    echo "    <ul>" >> "$index_file"

    # Listando os itens do diretório
    for item in "$dir"/*; do
        if [[ -e "$item" && "$(basename "$item")" != .* ]]; then
            if [[ -d "$item" || "$item" == *.pdf ]]; then
            	local name=$(basename "$item")
                echo "        <li><a href=\"$name\" style=\"display: block; text-decoration: none; color: inherit;\"><strong>$name</strong></a></li>" >> "$index_file"
            fi
	fi
    done

    # Fechamento do HTML
    echo "    </ul></section>" >> "$index_file"
    echo "</body>" >> "$index_file"
    echo "</html>" >> "$index_file"
}

# Percorrendo todos os subdiretórios e gerando index.html
find "$root_dir" -type d ! -path "*/.*" | while read -r subdir; do
    generate_index "$subdir"
done

echo "Arquivos index.html gerados com sucesso."

