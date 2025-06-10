Web Scraping dados da PNAD Contínua no google colab


# Neste script eu utilizo o pacote 'PNADcIBGE' para baixar os microdados da PNAD Contínua e o
# pacote 'googledrive' para fazer o upload automático para o Google Drive.
#-----------------------------------------------------------------------------

# Instalando os pacotes necessários para o download e manipulação dos dados.
install.packages(c("PNADcIBGE", "googledrive", "dplyr", "httr", "readr"))

# Carregando as bibliotecas necessárias.
library(PNADcIBGE)
library(googledrive)
library(dplyr)

# --- PASSO 1: Autenticação com o Google Drive ---
#
# ETAPA DE LIMPEZA: Limpando qualquer autenticação anterior.
cat("Limpando credenciais de autenticação antigas...\n")
drive_deauth()

# ETAPA DE AUTENTICAÇÃO: Iniciando um novo processo de login.
# O argumento 'scopes' solicita permissão total (leitura e escrita).

cat("Iniciando nova autenticação com o Google Drive...\n")
drive_auth(email = "mauricio.meira@ufv.br", scopes = "https://www.googleapis.com/auth/drive")
cat("Autenticação bem-sucedida.\n")


# --- PASSO 2: Definição de Parâmetros e Pasta no Google Drive ---

anos_de_interesse <- 2013:2023
nome_pasta_drive <- "Pnad_Contínua_2013-2023"

# Procura pela pasta no Google Drive para obter o ID.
pasta_destino_info <- drive_find(n_max = 1, q = paste0("name = '", nome_pasta_drive, "' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"))

if (nrow(pasta_destino_info) == 0) {
  stop(paste0("ERRO: A pasta '", nome_pasta_drive, "' não foi encontrada. Verifique o nome ou crie-a no seu Google Drive."))
}

id_pasta_drive <- pasta_destino_info$id
cat(paste0("Pasta '", nome_pasta_drive, "' encontrada com sucesso no Google Drive.\n"))


# --- PASSO 3: Download Temporário e Upload para o Google Drive ---

for (ano in anos_de_interesse) {
  for (trimestre in 1:4) {

    temp_dir <- file.path(tempdir(), paste0("pnadc_", ano, "_", trimestre))
    if (!dir.exists(temp_dir)) dir.create(temp_dir, recursive = TRUE)

    tryCatch({

      cat("--------------------------------------------------\n")
      cat(paste0("Processando: ", ano, " - Trimestre ", trimestre, "\n"))

      get_pnadc(year = ano, quarter = trimestre, savedir = temp_dir)

      arquivos_para_upload <- list.files(temp_dir, full.names = TRUE, recursive = TRUE)

      if (length(arquivos_para_upload) > 0) {
        cat("Iniciando upload para o Google Drive...\n")
        for (arquivo in arquivos_para_upload) {
          drive_upload(media = arquivo,
                       path = as_id(id_pasta_drive),
                       name = basename(arquivo),
                       overwrite = TRUE)
        }
        cat("Upload concluído para ", ano, "T", trimestre, ".\n")
      }

    }, error = function(e) {
      cat(paste0("AVISO: Não foi possível processar ", ano, "T", trimestre, ". Motivo: ", e$message, "\n"))
    }, finally = {
      cat("Limpando arquivos temporários...\n")
      unlink(temp_dir, recursive = TRUE)
    })

    Sys.sleep(1)
  }
}

cat("--------------------------------------------------\n")
cat("PROCESSO DE COLETA DE DADOS E UPLOAD CONCLUÍDO.\n")
cat("Todos os arquivos foram salvos na pasta '", nome_pasta_drive, "' no seu Google Drive.\n")

