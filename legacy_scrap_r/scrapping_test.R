rm(list = ls())
library(tidyverse)
library(lubridate)
library(rvest)

# Ddesde AGO 2005

nombre_mes <- c('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
nombre_fondo <- c('A','B','C','D','E')

ano <- 2020
mes <- 6
periodo <- lubridate::make_date(ano,mes,1)

url <- 'https://www.spensiones.cl/apps/rentabilidad/getRentabilidad.php?tiprent=FP'

web <- read_html(url)

tablas <- web %>% 
    html_nodes('table')

# Separo las tablas HTML por fondos
get_element_n <- as_mapper(~.x[[.y]])

fondo <- map(3:7, ~get_element_n(tablas,.x)) %>% 
    set_names(nombre_fondo)


# Elimino los primero 4 elementos
walk(fondo, ~xml_remove(xml_children(.x)[1:4])) 

# Creo tablas con respectivos header
cn <- c('afp','rentabilidad','acum_ano','acum_12_meses')

fondo <- map2_dfr(.x = fondo, 
                  .y = nombre_fondo, 
                  .f = ~{.x %>% html_table(header = F, dec = ',') %>% select(1:4) %>% set_names(cn) %>% mutate(mes = !!periodo, fondo = !!.y)})
