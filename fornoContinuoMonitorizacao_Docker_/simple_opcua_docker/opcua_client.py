#OPC-UA related:
from opcua import Client, ua
# from the folders
import classeUdc
import opacos
#Database related:
import psycopg2


# ======================================================================================================
# ----------------------------------- Read Opaque Values  ----------------------------------------------
# ======================================================================================================

# ---------------------- OPC UA CLIENT INITIALIZATION -----------------------------
# IP Address of uDC (endpoint url)
# Exemple: opc.tcp://LAPTOP-09I8AG5T:53530/OPCUA/SimulationServer
url = "opc.tcp://LAPTOP-09I8AG5T:53530/OPCUA/SimulationServer"

# namespace of the table where identifiers are
ns = 3

# Função que guarda o ultima hora para que apenas se insira dados de segundo a segundo
#last_value = datetime.datetime.now()

while True:

     # --------------------- Call function to read the values ---------------------------------
    # Arguments are:
    # url of the udc
    # Dictionary with --> name:identifier. Example: {"temp_zona1":"16F7600273308D29A6251453197CCC83"}
    # naspace index (ns) of the the values
    # It will return a dictionary. Example: {"temp_zona1":"854.13"}
    dados_carbo_mes     = classeUdc.udcReadOpaque(url, opacos.carbo_mes, ns)
    dados_carbo_con     = classeUdc.udcReadOpaque(url, opacos.carbo_con, ns)
    dados_preox_mes     = classeUdc.udcReadOpaque(url, opacos.preox_mes, ns)
    dados_preox_con     = classeUdc.udcReadOpaque(url, opacos.preox_con, ns)
    dados_rev_mes       = classeUdc.udcReadOpaque(url, opacos.rev_mes, ns)
    dados_rev_con       = classeUdc.udcReadOpaque(url, opacos.rev_con, ns)
    dados_tempera_mes   = classeUdc.udcReadOpaque(url, opacos.temp_mes, ns)
    dados_tempera_con   = classeUdc.udcReadOpaque(url, opacos.temp_con, ns)
    # ======================================================================================================
    # ----------------------------------- Insert Values to Postgres  ---------------------------------------
    # ======================================================================================================
    # Conection to database
    conn = psycopg2.connect(
        host="postgres",
        database="fornocontinuo",
        user="myuser",
        password="mypassword",
        port="5432")
    # Abrir o cursor ou pointer para a base de dados
    cur = conn.cursor()

    # gerar a query
    # inputs are: table name and data. "data" is a dictionary with the pair "column name":"value to insert"
    insert_query_carbo_mes     = classeUdc.generate_insert_query('public.carbo_mes', dados_carbo_mes)
    insert_query_carbo_con     = classeUdc.generate_insert_query('public.carbo_con', dados_carbo_con)
    insert_query_preox_mes     = classeUdc.generate_insert_query('public.preox_mes', dados_preox_mes)
    insert_query_preox_con     = classeUdc.generate_insert_query('public.preox_con', dados_preox_con)
    insert_query_rev_mes       = classeUdc.generate_insert_query('public.rev_mes', dados_rev_mes)
    insert_query_rev_con       = classeUdc.generate_insert_query('public.rev_con', dados_rev_con)
    insert_query_tempera_mes   = classeUdc.generate_insert_query('public.tempera_mes', dados_tempera_mes)
    insert_query_tempera_con   = classeUdc.generate_insert_query('public.tempera_con', dados_tempera_con)
    # Executar a query
    cur.execute(insert_query_carbo_mes)
    cur.execute(insert_query_carbo_con)
    cur.execute(insert_query_preox_mes)
    cur.execute(insert_query_preox_con)
    cur.execute(insert_query_rev_mes)
    cur.execute(insert_query_rev_con)
    cur.execute(insert_query_tempera_mes)
    cur.execute(insert_query_tempera_con)
    conn.commit()

    #Fechar as ligações à base de dados
    cur.close()
    conn.close()

