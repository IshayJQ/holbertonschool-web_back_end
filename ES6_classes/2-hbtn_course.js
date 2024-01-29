
export default class HolbertonCourse {
        constructor(name, length, students){
                 this.name = name;
                 this.length = lenght
                 this.students = students;
        }
        get name(){
            return htis._name;
        }
        set name(value){
             if (typeof value !== "string")
                  throw new typeError("Name must be a string")
             this._name = value;
        }

        get length(){
               return this._lenght;
        }

        set length(value){
              if (typeof value !== "string")
                   throw new typeError("Name must be a string")
              this._length = value;
        }

        get students(){
            return this._students
        }

        set students(value){
              if (typeof value !== "string")
                  
        } 
}
