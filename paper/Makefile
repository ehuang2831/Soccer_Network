TEX = pdflatex
TARGET = CS224W_ehuang_csandeep_soccer
BIB = bibtex
PDF = ps2pdf
PS = dvips
RM = rm -rf
all:
	$(TEX) $(TARGET).tex
	$(BIB) $(TARGET).aux
	$(TEX) $(TARGET).tex
	$(TEX) $(TARGET).tex
	#$(PS) -t letter $(TARGET).dvi
	#$(PDF) -sPAPERSIZE=letter $(TARGET).ps
clean:
	$(RM) $(TARGET).out $(TARGET).aux $(TARGET).bbl $(TARGET).dvi $(TARGET).pdf $(TARGET).blg $(TARGET).log $(TARGET).ps
