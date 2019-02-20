import { Component, OnInit } from '@angular/core';
import {HelloService} from './hello.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-hello',
  templateUrl: './hello.component.html',
  styleUrls: ['./hello.component.css']
})
export class HelloComponent implements OnInit {
  hello:string;
  constructor(private helloService: HelloService, private router: Router) { }

  ngOnInit() {
    this.gethellodata();
  }
  gethellodata(){
    this.helloService.getHello().subscribe((data:any) => {//data:any is what is returned
      this.hello = data;
      console.log('Data requested ... ');
      console.log(this.hello);
    });
    console.log("got data"+this.hello)
    
  }


}
