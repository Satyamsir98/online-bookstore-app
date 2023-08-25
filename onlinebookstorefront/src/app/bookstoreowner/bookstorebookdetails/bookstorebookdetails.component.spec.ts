import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookstorebookdetailsComponent } from './bookstorebookdetails.component';

describe('BookstorebookdetailsComponent', () => {
  let component: BookstorebookdetailsComponent;
  let fixture: ComponentFixture<BookstorebookdetailsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BookstorebookdetailsComponent]
    });
    fixture = TestBed.createComponent(BookstorebookdetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
