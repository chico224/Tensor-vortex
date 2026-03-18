import ast
import inspect
import logging

logger = logging.getLogger("CodeMutator")

class DynamicStrategyMutator:
    """
    AUTO-MUTATION CORE (Singularité Algorithmique).
    Peut lire une logique de trading texte (ex: du PDF), 
    générer un Abstract Syntax Tree (AST) Python, et le compiler
    à la volée en RAM (Hot-Swapping) pour rajouter une stratégie
    sans jamais éteindre le bot.
    """
    def __init__(self, experts_module):
        self.experts = experts_module
        
    def execute_mutation(self, name, logic_string):
        """
        Injecte un nouveau code Python dans l'instance Experts.
        logic_string: Le code source (texte) d'une fonction Python.
        """
        logger.warning(f"🧬 MUTATION DÉCLENCHÉE : Création de l'expert '{name}' en RAM...")
        try:
            # Sécurité 1: Compiler le string en AST pour valider la syntaxe
            parsed_ast = ast.parse(logic_string)
            
            # Sécurité 2: Compilation Bytecode
            compiled_code = compile(parsed_ast, filename=f"<mutation_{name}>", mode="exec")
            
            # 3. Exécution dans un namespace isolé
            namespace = {}
            exec(compiled_code, globals(), namespace)
            
            # 4. Extraction de la fonction (on suppose qu'elle s'appelle 'expert_function')
            if 'expert_function' in namespace:
                new_expert = namespace['expert_function']
                # Hot-swap direct dans la liste des experts du QuantEngine !
                self.experts.append(new_expert)
                logger.info(f"✅ Mutation Réussie. Expert {name} actif.")
                return True
            else:
                logger.error("Échec de Mutation : Aucune 'expert_function' trouvée dans le code.")
                return False
                
        except Exception as e:
            logger.critical(f"ERREUR FATALE LORS DE LA MUTATION : {e}")
            return False

# Exemple de logic_string :
# """
# def expert_function(indicators):
#     if indicators['close'][-1] > indicators['sma_200'][-1]: return 1
#     if indicators['close'][-1] < indicators['sma_200'][-1]: return -1
#     return 0
# """
