Rails.application.routes.draw do
  get  'btests/:yr', to: 'btests#index'
  get  'posts/index'
  root 'posts#index'
  get  ':controller(/:action)'
  # get ':controller(/:action(/:id(.:format)))'
  get 'about'     => 'posts#about'
  get 'blog'      => 'posts#blog'
  get 'contact'   => 'posts#contact'
  get 'backtests' => 'posts#backtests'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
