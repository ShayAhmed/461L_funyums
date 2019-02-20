import {Injectable} from '@angular/core';
import {HttpClient,HttpResponse,HttpRequest,HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class HelloService{

    url:"http://127.0.0.1:5000/v1";
    constructor(private http:HttpClient){
    }
    getHello():Observable<any>{
        console.log("getting data from backend")
        //return this.http.get('${this.url}/hello')
        return this.http.get("http://127.0.0.1:5000/v1"+"/hello")
    }
    
}