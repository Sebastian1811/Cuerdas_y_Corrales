from tablero import *
from copy import deepcopy

def valorHeuristico(TableroActual):
        heuristica = TableroActual.puntajeJugadorMax - TableroActual.puntajeJugadorMin
        return heuristica

def minimax(TableroActual, jugadasDisponibles, profundidadArbol, min_max):
        # The value of bestMove defaults to -inf for a Max layer, and +inf for a Min Layer
        if min_max is True:
            bestMove = (-1000000, None)
        else:
            bestMove = (1000000, None)

        
        if profundidadArbol == 0 or len(jugadasDisponibles) == 0: # se alcanza la profundidad del arbol o no hay mas jugadas disponibles
            heuristica = valorHeuristico(TableroActual)
            return (heuristica, None)

        # Get successors
        for i in range(0, len(jugadasDisponibles)):
            # Retrieve coordinates of current successor TableroActual
            jugada = jugadasDisponibles.pop()

            # Create a deep copy of the TableroActual to be explored
            TableroActualCopy = deepcopy(TableroActual)
            jugadasDisponiblesCopy = deepcopy(jugadasDisponibles)
            TableroActualCopy.jugada(jugada, min_max)

            # Add the coordinates back onto the openVector list, this ensures subsequent
            # child TableroActuals at the current depth can fully explore the remainder of the tree
            jugadasDisponibles.appendleft(jugada)

            # valorMax-valorMin Pruning
            # We check the requisite value (valorMin on a max node, valorMax on a min) before
            # exploring the nodes children. If a violation is detected, this path returns.
            heuristica = valorHeuristico(TableroActualCopy)
            #podaAlfaBeta(TableroActualCopy,jugada,min_max,heuristica)
            if min_max:
                if heuristica >= TableroActualCopy.valorMin:
                    return (heuristica, jugada)
                else:
                    TableroActualCopy.valorMax = max(TableroActualCopy.valorMax, heuristica)
            else:
                if heuristica <= TableroActualCopy.valorMax:
                    return (heuristica, jugada)
                else:
                    TableroActualCopy.valorMin = min(TableroActualCopy.valorMin, heuristica)

            # Make a recursive call to the minimax function with the child TableroActual
            # The goal TableroActual is back propagated up the tree upon the end of recursion,
            # IE, when profundidadArbol limit is reached or the open moves are exhausted
            nextMove = minimax(TableroActualCopy, jugadasDisponiblesCopy, profundidadArbol - 1, not min_max)

            # Check the score returned from the child TableroActual against the 'bestScore'
            if min_max is True:
                # At a max level, we seek scores higher than the current max
                if nextMove[0] > bestMove[0]:
                    bestMove = (nextMove[0], jugada)
            else:
                # At a min level, we seek scores lower than the current max
                if nextMove[0] < bestMove[0]:
                    bestMove = (nextMove[0], jugada)
        return bestMove


