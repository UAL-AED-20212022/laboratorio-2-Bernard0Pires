from re import A
from models.LinkedList import LinkedList


def main():

    country_list = LinkedList()
    while True:
        user_comand:list[str] = input().split(" ")   

        if user_comand[0] in ["RPI", "RPF", "RPDE", "RPAE", "RPII", "VNE", "VP", "EPE", "EUE", "EP"]:
            if user_comand[0] == "RPI":
                country_to_add:str = user_comand[1]
                country_list.insert_at_start(country_to_add)
                country_list.traverse_list()

            if user_comand[0] == "RPF":
                country_to_add:str = user_comand[1]
                country_list.insert_at_end(country_to_add)
                country_list.traverse_list()
            
            if user_comand[0] == "RPDE":
                country_to_add:str = user_comand[1]
                reference_country:str = user_comand[2]
                country_list.insert_after_item(reference_country, country_to_add)
                country_list.traverse_list()

            if user_comand[0] == "RPAE":
                country_to_add:str = user_comand[1]
                reference_country:str = user_comand[2]
                country_list.insert_before_item(reference_country, country_to_add)
                country_list.traverse_list()

            if user_comand[0] == "RPII":
                country_to_add:str = user_comand[1]
                desired_index:int = int(user_comand[2])
                country_list.insert_at_index(desired_index, country_to_add)
                country_list.traverse_list()
            
            if user_comand[0] == "VNE":
                number_of_elements:int = country_list.get_count()
                print(f"O número de elementos são {number_of_elements}.")
            
            if user_comand[0] == "VP":
                country_to_search:str = user_comand[1]
                country_to_search_error:bool = country_list.search_item(country_to_search)  #Variável de controlo que retorna se o país se encontra na lista(True) ou não (False).

                if country_to_search_error == True:
                    print(f"O país {country_to_search} encontra-se na lista.")
                
                if country_to_search_error == False:
                    print(f"O país {country_to_search} não se encontra na lista.")
        
            if user_comand[0] == "EPE":
                country_to_eliminate:str = country_list.start_node.get_item()  #Variável que obtém o primeiro elemento da lista para, após a sua eliminação, dar print do elemento eliminado.
                country_list.delete_at_start()
                print(f"O país {country_to_eliminate} foi eliminado da lista.")

            if user_comand[0] == "EUE":
                country_to_eliminate:str = country_list.get_last_node()     #Variável que obtém o último elemento da lista para, após a sua eliminação, dar print do elemento eliminado.
                country_list.delete_at_end()
                print(f"O país {country_to_eliminate} foi eliminado da lista.")

            if user_comand[0] == "EP":
                country_to_eliminate:str = user_comand[1]
                check_country_in_list:bool = country_list.search_item(country_to_eliminate) #Variável de controlo que retorna True, caso o país se encontre na lista e, de seguida, é eliminado.
                
                if check_country_in_list == False:
                    print(f"O país {country_to_eliminate} não se encontra na lista.")

                if check_country_in_list == True:
                    country_list.delete_element_by_value(country_to_eliminate)
                    print(f"O país {country_to_eliminate} foi eliminado da lista.")

        else: 
            pass 