
function PerlinNoise2DArray(WorldSizePow, PerlinPitchWeight, WorldHeight){

    const PerlinArrXLow = PerlinNoiseArray(WorldSizePow, PerlinPitchWeight)
    const PerlinArrXHigh = PerlinNoiseArray(WorldSizePow, PerlinPitchWeight)

    const PerlinArrYLow = PerlinNoiseArray(WorldSizePow, PerlinPitchWeight)
    const PerlinArrYHigh = PerlinNoiseArray(WorldSizePow, PerlinPitchWeight)

    // [x][y]
    let PerlinNoise2DArray = []

    for (let x = 0; x < PerlinArrYHigh.length; x++) {
        PerlinNoise2DArray[x] = []
        for (let y = 0; y < PerlinArrXHigh.length; y++) {
            // X coord value
            const LinearInterpolateXValue = PerlinArrYLow[x] + ((y / (PerlinArrXLow.length)) * (PerlinArrYHigh[x] - PerlinArrYLow[x]))

            // Y coord value
            const LinearInterpolateYValue = PerlinArrXLow[y] + ((x / (PerlinArrYLow.length)) * (PerlinArrXHigh[y] - PerlinArrXLow[y]))

            PerlinNoise2DArray[x][y] = (LinearInterpolateXValue + LinearInterpolateYValue) / 2
        }
    }

    for (let i = 0; i < PerlinNoise2DArray.length; i++) {

        PerlinNoise2DArray[i] = PerlinNoise2DArray[i].map(function (num){return Math.ceil(num * WorldHeight)})

    }

    return PerlinNoise2DArray

}



function PerlinNoiseArray(ArrSizePow, PitchWeight){

    const ArrLength = Math.pow(2, ArrSizePow)

    let SeedArray = RandomArray(ArrLength)

    let Multiplier = 1

    let TotDivide = 0

    // Prepare Perlin Array
    let PerlinArray = []
    for (let i = 0; i < ArrLength; i++) {PerlinArray[i] = 0}

    for (let i = 1; i <= ArrSizePow; i++) {

        const PitchDiv = ArrLength / (Math.pow(2,i))

        Multiplier /= PitchWeight

        TotDivide += Multiplier

        let PitchArr = []

        for (let o = 0; o < (Math.pow(2,i)); o++) {

            // PerlinArray[PitchDiv * o] += SeedArray[PitchDiv * o] * Multiplier

            PitchArr[PitchDiv * o] = SeedArray[PitchDiv * o]
        }

        // Går igenom varje indexvärde i Pitcharr för att söka efter närmaste värden och linear interpolate:a
        for (let o = 0; o < ArrLength; o++) {
            if(PitchArr[o]){continue}

            let IndexLow = o
            let IndexLowIndexOffsetTracker = 0

            while(PitchArr[IndexLow] == undefined){
                IndexLow--
                IndexLowIndexOffsetTracker--
                if(IndexLow < 0){IndexLow = ArrLength-1}
            }

            let IndexHigh = o
            let IndexHighIndexOffsetTracker = 0

            while(PitchArr[IndexHigh] == undefined){
                IndexHigh++
                IndexHighIndexOffsetTracker++
                if(IndexHigh > ArrLength){IndexHigh = 0}
            }

            const IndexHighIndexOffset = o - IndexHighIndexOffsetTracker
            const IndexLowIndexOffset = o - IndexLowIndexOffsetTracker

            const IndexLowVal = PitchArr[IndexLow]
            const IndexHighVal = PitchArr[IndexHigh]

            const CalculatedValueO = IndexLowVal + ((IndexHighVal - IndexLowVal) * ((o - IndexLowIndexOffset) / (IndexHighIndexOffset - IndexLowIndexOffset)))

            PitchArr[o] = CalculatedValueO

        }

        for (let o = 0; o < ArrLength; o++) {

            PerlinArray[o] += PitchArr[o] * Multiplier
            
        }

        

    }

    PerlinArray = PerlinArray.map(function (num){return (num / TotDivide)})

    return PerlinArray

}



function RandomArray(ArrLength){
    let RandArr = []
    for (let i = 0; i < ArrLength; i++) {
        RandArr.push(Math.random())
    }
    return RandArr
}