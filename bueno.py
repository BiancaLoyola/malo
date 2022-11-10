with open("./cero.js","w") as f:
    f.write("""const malo = () => {
    console.log('hola');
    alert('uno');
};
malo()""")
    f.close()