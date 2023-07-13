import pandas as pd

# Cria um DataFrame vazio com as colunas desejadas
df = pd.DataFrame(columns=[
    'Ano', 'Marca', 'Modelo', 'Versão', 'Preço (Seminovos tabela KBB)', 'Preço parametro', 'Preço do IPVA',
    'Valor médio de revisões', 'Tempo de garantia', 'Câmbio', 'Categoria', 'Porte', 'Seguimento', 'Propulsão',
    'Motorização', 'Cilindros', 'Potência', 'Torque', 'Velocidade Máxima', '0-100', 'Consumo Parametrizado',
    'Consumo cidade (Km/L)', 'Consumo Estrada (Km/L)', 'Autonomia Urbana', 'Autonomia Estrada', 'Tração', 'Direção',
    'Suspensão dianteira', 'Suspensão Traseira', 'Freios Dianteiros', 'Freios Traseiros',
    'Itens de segurança', 'Itens de Conforto', 'Itens de Infotenimento', 'Portas', 'Lugares', 'Altura', 'Largura',
    'Comprimento', 'Peso', 'Tanque', 'Entre Eixos', 'Litragem real do porta malas', 'Pneus Dianteiros',
    'Pneus Traseiros', 'Estepe', 'Principais destaques do veículo', 'Justificativa padrão',
    'Pontos Positivos', 'Pontos Negativos', 'Problemas Crônicos', 'Facilidade de Revenda', 'Informações de mercado',
    'Reposição de peças', 'Mêcanica', 'Segurança', 'Conforto', 'Tecnologia', 'Performance', 'Consumo',
    'Acabamento', 'Espaço Interno', 'Custo-beneficio', 'Avaliação Geral'
])

df.to_excel('dados_carros.xlsx', index=False)