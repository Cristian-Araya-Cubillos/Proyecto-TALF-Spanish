# Generated from C:/Users/Yukihana/IdeaProjects/Trabajo/src/recipes.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .recipesParser import recipesParser
else:
    from recipesParser import recipesParser

# This class defines a complete generic visitor for a parse tree produced by recipesParser.

class recipesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by recipesParser#consulta.
    def visitConsulta(self, ctx:recipesParser.ConsultaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by recipesParser#condicion.
    def visitCondicion(self, ctx:recipesParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by recipesParser#ingrediente.
    def visitIngrediente(self, ctx:recipesParser.IngredienteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by recipesParser#cantidad.
    def visitCantidad(self, ctx:recipesParser.CantidadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by recipesParser#descriptor.
    def visitDescriptor(self, ctx:recipesParser.DescriptorContext):
        return self.visitChildren(ctx)



del recipesParser