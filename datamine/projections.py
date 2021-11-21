from _typeshed import ReadableBuffer
from .static import Static

class Projections(): 
    projDict = Static.posScoringDict

    def rbProjection(self, rushYds, rushTds, recYds, recTds, rec, fum):
        ratio = self.projDict['rb']
        proj = (rushYds * ratio["rushYds"] 
                + rushTds * ratio['rushTds']
                + recYds * ratio['recYds']
                + recTds * ratio['recTds']
                + rec * ratio['rec']
                + fum * ratio['fum'])
        return  proj

    def wrProjection(self, rushYds, rushTds, recYds, recTds, rec, fum):
        ratio = self.projDict['wr']
        proj = (rushYds * ratio["rushYds"] 
                + rushTds * ratio['rushTds']
                + recYds * ratio['recYds']
                + recTds * ratio['recTds']
                + rec * ratio['rec']
                + fum * ratio['fum'])
        return  proj

    def teProjection(self, recYds, recTds, rec, fum):
        ratio = self.projDict['te']
        proj = (recYds * ratio['recYds']
                + recTds * ratio['recTds']
                + rec * ratio['rec']
                + fum * ratio['fum'])
        return  proj
    
    def qbProjection(self, paYds, paTds, ints, rushYds, rushTds, fum):
        ratio = self.projDict['qb']
        proj = (paYds * ratio['paYds']
                + paTds * ratio['paTds']
                + ints * ratio['ints']
                + rushYds * ratio['rushYds']
                + rushTds * ratio['rushTds']
                + fum * ratio['fum'])
    def kProjection(kproj):
        return kproj

    def kProjection(dproj):
        return dproj
