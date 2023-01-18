from opcua import Client, ua
from datetime import datetime

def udcReadOpaque(url, opaques_dictionary, nsindex):

    # ---------------------- Connection to the udc Client -----------------------------
    client = Client(url)

    # connect opc ua client to opc ua server
    client.connect()

    # Reatrive the dictionary keys (key:atribute) for the loop
    # dictionary.keys() method does not return a list datatype. You need to transform it to a list
    #so it can be readable by the ua.NodeID()
    names = list(opaques_dictionary.keys())

    # Get current date and time
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    # init. the dictionary to store values
    dictionary = {"date": current_date, "time": current_time}

    # loops each node to:
    #  1- Get the values of the nodes
    #  2- Add them to a dictionary for easy readbility
    for k in range(len(opaques_dictionary)):

        # Get_node(Creates a object of the specific node)
        # get_value(gets the value of the spectific node)
        # ns is the designated namespace
        # opaques_dictionary[names[k]] will return the 'CD13505F9F8FAB725DDFA5DC534FCE08' opaque identifier
        valores_opacos = client.get_node(
            ua.NodeId(bytes.fromhex(opaques_dictionary[names[k]]), nsindex)).get_value()

        # add each entry to dictionary with format {"name_assaigned" : "current_value"}
        # example: {"temp_zona1":"854.13"}
        dictionary[names[k]] = valores_opacos

    # client.close_session()
    client.disconnect()

    #Debug
    print("\n\n")
    print(dictionary)
    print("\n\n")

    #Return
    return dictionary

# ======================================================================================================
# ----------------------------------- Genarates the INSERT string for postres  -------------------------
# ======================================================================================================

#Inputs:
# table_name --> nome da tablea
# column_names --> nomes das colunas
# values --> valores para as respetivas colunas
def generate_insert_query(table_name, data):

    # vai buscar os nomes que estão no dicionário para criar as colunas da tabela
    column_names = list(data.keys())
    # Isto é uma chamada "list comprehension"
    #which is a concise way of applying a transformation to 
    #each element of an iterable object and creating a new list from the transformed elements
    # Ainda aplica a função str() para fazer um cast aos valores que são int passarem a string
    #agora, faz a junção dos nomes das colunas. O round() arredonda para duas casas decimais.
    values = []
    for key, value in data.items():
        if key in ['date', 'time']:
            values.append("'{}'".format(value))
        else:
            values.append(str(round(value, 2)))

    # join faz pega em um array e junta-o em uma string com o separador indicado antes do .join
    # 'separador'.join([1,2,3])
    column_names_string = ', '.join(column_names)
    values_string = ', '.join(values)

    # colocar as variáveis na string com placeholders prórprios para as receber
    sql_string = f"INSERT INTO {table_name}({column_names_string}) VALUES({values_string});"   

    #retorna a string INSERT parametrizada
    # Exemplo: "INSERT INTO test(data,hota,tempzona1) VALUES (NOW(),NOW(), 830.41)"
    print("\n\n")
    print(sql_string)
    print("\n\n")
    return sql_string