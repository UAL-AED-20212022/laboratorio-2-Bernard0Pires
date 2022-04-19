from re import A
from models.LinkedList import LinkedList
from models.Node import Node


def main():

    country_list = LinkedList()
    while True:
        user_comand:list[str] = input().lower().split(" ")   

        if user_comand[0] in ["rpi", "rpf", "rpde", "rpae", "rpii", "vne", "vp", "epe", "eue", "ep"]:
            if user_comand[0] == "rpi":
                country_to_add:str = user_comand[1]
                country_list.insert_at_start(country_to_add)
                country_list.traverse_list()

            if user_comand[0] == "rpf":
                country_to_add:str = user_comand[1]
                country_list.insert_at_end(country_to_add)
                country_list.traverse_list()
            
            if user_comand[0] == "rpde":
                country_to_add:str = user_comand[1]
                reference_country:str = user_comand[2]
                country_list.insert_after_item(reference_country, country_to_add)
                country_list.traverse_list()

            if user_comand[0] == "rpae":
                country_to_add:str = user_comand[1]
                reference_country:str = user_comand[2]
                country_list.insert_before_item(reference_country, country_to_add)
                country_list.traverse_list()

            if user_comand[0] == "rpii":
                country_to_add:str = user_comand[1]
                desired_index:int = int(user_comand[2])
                country_list.insert_at_index(desired_index, country_to_add)
                country_list.traverse_list()
            
            if user_comand[0] == "vne":
                number_of_elements:int = country_list.get_count()
                print(f"O número de elementos são {number_of_elements}")
            
            if user_comand[0] == "vp":
                country_to_search:str = user_comand[1]
                country_to_search_error:bool = country_list.search_item(country_to_search)

                if country_to_search_error == True:
                    print(f"O país {country_to_search} encontra-se na lista.")
                
                if country_to_search_error == False:
                    print(f"O país {country_to_search} não se encontra na lista.")
        
            if user_comand[0] == "epe":
                country_to_eliminate:str = country_list.start_node.get_item()
                country_list.delete_at_start()
                print(f"O país {country_to_eliminate} foi eliminado da lista.")

            if user_comand[0] == "eue":
                country_to_eliminate:str = country_list.get_last_node()
                country_list.delete_at_end()
                print(f"O país {country_to_eliminate} foi eliminado da lista.")

            if user_comand[0] == "ep":
                country_to_eliminate:str = user_comand[1]
                check_country_in_list:bool = country_list.search_item(country_to_eliminate)
                
                if check_country_in_list == False:
                    print(f"O país {country_to_eliminate} não se encontra na lista.")

                if check_country_in_list == True:
                    country_list.delete_element_by_value(country_to_eliminate)
                    print(f"O país {country_to_eliminate} foi eliminado da lista.")

        else: 
            pass 