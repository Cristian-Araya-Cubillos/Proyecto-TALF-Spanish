# Generated from C:/Users/Yukihana/IdeaProjects/Trabajo/src/recipes.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .recipesParser import recipesParser
else:
    from recipesParser import recipesParser

# This class defines a complete listener for a parse tree produced by recipesParser.
class recipesListener(ParseTreeListener):

    # Enter a parse tree produced by recipesParser#consulta.
    def enterConsulta(self, ctx:recipesParser.ConsultaContext):
        pass

    # Exit a parse tree produced by recipesParser#consulta.
    def exitConsulta(self, ctx:recipesParser.ConsultaContext):
        pass


    # Enter a parse tree produced by recipesParser#condicion.
    def enterCondicion(self, ctx:recipesParser.CondicionContext):
        pass

    # Exit a parse tree produced by recipesParser#condicion.
    def exitCondicion(self, ctx:recipesParser.CondicionContext):
        pass


    # Enter a parse tree produced by recipesParser#ingrediente.
    def enterIngrediente(self, ctx:recipesParser.IngredienteContext):
        pass

    # Exit a parse tree produced by recipesParser#ingrediente.
    def exitIngrediente(self, ctx:recipesParser.IngredienteContext):
        pass


    # Enter a parse tree produced by recipesParser#cantidad.
    def enterCantidad(self, ctx:recipesParser.CantidadContext):
        pass

    # Exit a parse tree produced by recipesParser#cantidad.
    def exitCantidad(self, ctx:recipesParser.CantidadContext):
        pass


    # Enter a parse tree produced by recipesParser#descriptor.
    def enterDescriptor(self, ctx:recipesParser.DescriptorContext):
        pass

    # Exit a parse tree produced by recipesParser#descriptor.
    def exitDescriptor(self, ctx:recipesParser.DescriptorContext):
        pass



del recipesParser