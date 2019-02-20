import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HelloComponent} from './hello/hello.component';

const routes: Routes = [
  { path: 'hello', component: HelloComponent },
  {path:"**",component:HelloComponent}
  //{ path: '', redirectTo: '/hello', pathMatch: 'full'}
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
