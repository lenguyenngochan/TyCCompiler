# Generated from D:/tyc-compiler-main/tyc-compiler-main/src/grammar/TyC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete generic visitor for a parse tree produced by TyCParser.

class TyCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TyCParser#program.
    def visitProgram(self, ctx:TyCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#declist.
    def visitDeclist(self, ctx:TyCParser.DeclistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#decl.
    def visitDecl(self, ctx:TyCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#primitive_type.
    def visitPrimitive_type(self, ctx:TyCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#type.
    def visitType(self, ctx:TyCParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#init.
    def visitInit(self, ctx:TyCParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#memstructlst.
    def visitMemstructlst(self, ctx:TyCParser.MemstructlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#structdecl.
    def visitStructdecl(self, ctx:TyCParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#structmemacc.
    def visitStructmemacc(self, ctx:TyCParser.StructmemaccContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#vardecl_no_init.
    def visitVardecl_no_init(self, ctx:TyCParser.Vardecl_no_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#vardecl_with_init.
    def visitVardecl_with_init(self, ctx:TyCParser.Vardecl_with_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#vardecl.
    def visitVardecl(self, ctx:TyCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#funcdecl.
    def visitFuncdecl(self, ctx:TyCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#param.
    def visitParam(self, ctx:TyCParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#paramprime.
    def visitParamprime(self, ctx:TyCParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#paramlist.
    def visitParamlist(self, ctx:TyCParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#ass.
    def visitAss(self, ctx:TyCParser.AssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#lhs.
    def visitLhs(self, ctx:TyCParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#stmtlist.
    def visitStmtlist(self, ctx:TyCParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#stmt.
    def visitStmt(self, ctx:TyCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#vardeclstmt.
    def visitVardeclstmt(self, ctx:TyCParser.VardeclstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#blockstmt.
    def visitBlockstmt(self, ctx:TyCParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#asstmt.
    def visitAsstmt(self, ctx:TyCParser.AsstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#ifstmt.
    def visitIfstmt(self, ctx:TyCParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#whilestmt.
    def visitWhilestmt(self, ctx:TyCParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#forstmt.
    def visitForstmt(self, ctx:TyCParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_init.
    def visitFor_init(self, ctx:TyCParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_exp.
    def visitFor_exp(self, ctx:TyCParser.For_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#caseclause.
    def visitCaseclause(self, ctx:TyCParser.CaseclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#caselist.
    def visitCaselist(self, ctx:TyCParser.CaselistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#switchstmt.
    def visitSwitchstmt(self, ctx:TyCParser.SwitchstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#breakstmt.
    def visitBreakstmt(self, ctx:TyCParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#contstmt.
    def visitContstmt(self, ctx:TyCParser.ContstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#retstmt.
    def visitRetstmt(self, ctx:TyCParser.RetstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expstmt.
    def visitExpstmt(self, ctx:TyCParser.ExpstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp.
    def visitExp(self, ctx:TyCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp1.
    def visitExp1(self, ctx:TyCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp2.
    def visitExp2(self, ctx:TyCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp3.
    def visitExp3(self, ctx:TyCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp4.
    def visitExp4(self, ctx:TyCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp5.
    def visitExp5(self, ctx:TyCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp6.
    def visitExp6(self, ctx:TyCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp7.
    def visitExp7(self, ctx:TyCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp8.
    def visitExp8(self, ctx:TyCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp9.
    def visitExp9(self, ctx:TyCParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp10.
    def visitExp10(self, ctx:TyCParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#exp11.
    def visitExp11(self, ctx:TyCParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#arglist.
    def visitArglist(self, ctx:TyCParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#argprime.
    def visitArgprime(self, ctx:TyCParser.ArgprimeContext):
        return self.visitChildren(ctx)



del TyCParser