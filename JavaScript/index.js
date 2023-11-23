const mtx = {}

function generateNumber()
{
    let result = Math.random();
    if(result > 0,5)
    {
        return 1;
    }else return 0;
}

function generateIndividual()
{

    return {
        peso1: generateNumber(),
        peso2: generateNumber(),
        entrada1: generateNumber(),
        entrada2: generateNumber()
        };
}

function generatePopulation()
{
    const x = 10;
    for(let i = 0; i < x; i++)
    {
        mtx.push(generateIndividual());
    }
    return mtx
}

function aptitudeTest(mtx)
{
    for(var i = 0; i < 6; i++)
    {
        const randomIndividual = parseInt(Math.random(mtx.length))
        //passedAptitude.push(mtx[randomIndividual])
        mtx.splice(randomIndividual, 1)
    }
    return mtx
}

function selection()
{
    const half = mtx.slice(0,1)
    const otherhalf = mtx.slice(2,3)
    const mutants = createMutation(otherhalf)
    const children = createCrossover(half)
    mtx.push(children, mutants)
}

function createMutation(arr)
{
    
    arr.forEach(element => {
        const r = parseInt(Math.random(4))
        switch (r) {
            case 1:
                element.peso1 == 1 ? 0 : 1
                break;
            case 2:
                element.peso2 == 1 ? 0 : 1
                break;
            case 3:
                element.entrada1 == 1 ? 0 : 1
                break;
            case 1:
                element.entrada2 == 1 ? 0 : 1
                break;
            default:
                break;
        }
    });
}

function createCrossover(array)
{
    const children = [];
    for (let i = 0; i < array.length; i++)
    {
        const father = array[i];
        i++;
        const mother = array[i];
        let child1 = {
            peso1: mother.peso1 === 1 ? 0 : 1,
            entrada1: mother.entrada1 === 1 ? 0 : 1,
            peso2: father.peso2,
            entrada2: father.entrada2
        };

        let child2 = {
            peso1: father.peso1 === 1 ? 0 : 1,
            entrada1: father.entrada1 === 1 ? 0 : 1,
            peso2: mother.peso2,
            entrada2: mother.entrada2
        };
        children.push(child1, child2)
    }
    return array
}

generatePopulation()