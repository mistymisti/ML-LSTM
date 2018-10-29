var fs = require('fs')
var  ps = require('python-shell')

let options = {
    mode: 'text',
    args: ['./Files/input.csv']
}

fs.watchFile('./Files/input.csv',(curr,prev) => {
    ps.PythonShell.run('classifyScript.py', options, function(err, results){
        if(err) throw err;
    })
})