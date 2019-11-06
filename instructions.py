'''
#Creates GHZ([Shraddha, Sothy, FM, Fred]) out of our 5 nodes network

    FM         STAREXP  Georg, [FM] 
    Georg      STAREXP  FM,    [Fred, Sothy]
    Fred       STAREXP  Georg, [Fred]
    Sothy      STAREXP  Georg, [Sothy, Shraddha]
    Shraddha   STAREXP  Sothy,[Shraddha]

'''

'''
Place STAREXP Source, Targets

if Targets==[Place] : # (aka do nothing)
    FinalQubit=qubit[Source]

else:
    if Place in Targets:
        qubit[Place]=CreateQubit()
    Auxqubit=CreateQubit()
    Auxqubit.cphase(qubit[Source])
    for t in Targets: Auxqubit.cphase(qubit[t])
    Auxqubit.measureY()
    qubit[Source].measureY()
    for t in Targets:
        if t != Place:
            qubit[t].measureY()
        else:
            FinalQubit=qubit[t]

'''
