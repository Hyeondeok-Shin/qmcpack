#ifdef COMPILATION_INSTRUCTIONS//-*-indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4-*-
$CXX -D_TEST_MULTI_MEMORY_ADAPTORS_CUDA_PTR $0 -o $0x -lcudart -lboost_unit_test_framework&&$0x&&rm $0x; exit
#endif

#ifndef BOOST_MULTI_MEMORY_ADAPTORS_CUDA_PTR_HPP
#define BOOST_MULTI_MEMORY_ADAPTORS_CUDA_PTR_HPP

#ifndef HD
#if defined(__CUDACC__)
#define HD __host__ __device__
#else
#define HD 
#endif
#endif

#include "../../adaptors/cuda/clib.hpp"
#include "../../adaptors/cuda/error.hpp"

#include<cassert> // debug
#include<utility> // exchange

#ifndef _DISABLE_CUDA_SLOW
#ifdef NDEBUG
#define SLOW deprecated("WARNING: slow memory operation")
#else
#define SLOW
#endif
#else
#define SLOW
#endif

#define BEGIN_NO_DEPRECATED \
\
_Pragma("GCC diagnostic push") \
_Pragma("GCC diagnostic ignored \"-Wdeprecated-declarations\"") \
\

#define END_NO_DEPRECATED \
\
_Pragma("GCC diagnostic pop") \
\

#define BEGIN_CUDA_SLOW BEGIN_NO_DEPRECATED
#define END_CUDA_SLOW   END_NO_DEPRECATED

#define NO_DEPRECATED(ExpR) \
	BEGIN_NO_DEPRECATED \
	ExpR \
	END_NO_DEPRECATED

#define CUDA_SLOW(ExpR) NO_DEPRECATED(ExpR)

namespace boost{namespace multi{
namespace memory{namespace cuda{

template<class T> struct ref;

template<typename T, typename Ptr = T*> struct ptr;

#if 1
template<typename RawPtr>
struct ptr<void const, RawPtr>{ // used by memcpy
	using raw_pointer = RawPtr;
private:
	raw_pointer rp_;
	template<typename, typename> friend struct ptr;
	template<class TT> friend ptr<TT> const_pointer_cast(ptr<TT const> const&);
	ptr(raw_pointer rp) : rp_{rp}{}
public:
	ptr() = default;
	ptr(ptr const&) = default;
	ptr(std::nullptr_t n) : rp_{n}{}
	template<class Other, typename = decltype(raw_pointer{std::declval<Other const&>().rp_})>
	ptr(Other const& o) : rp_{o.rp_}{}
	ptr& operator=(ptr const&) = default;

	using pointer = ptr;
	using element_type = typename std::pointer_traits<raw_pointer>::element_type;
	using difference_type = void;//typename std::pointer_traits<impl_t>::difference_type;
	explicit operator bool() const{return rp_;}
//	explicit operator impl_t&()&{return impl_;}
	bool operator==(ptr const& other) const{return rp_==other.rp_;}
	bool operator!=(ptr const& other) const{return rp_!=other.rp_;}
	friend ptr to_address(ptr const& p){return p;}
};
#endif

namespace managed{
	template<typename T, typename RawPtr> struct ptr;
}

template<class T> class allocator;

template<typename RawPtr>
struct ptr<void, RawPtr>{
protected:
	using T = void;
	using raw_pointer = RawPtr;
	using raw_pointer_traits = std::pointer_traits<raw_pointer>;
	static_assert(std::is_same<void, typename raw_pointer_traits::element_type>{}, "!");
	raw_pointer rp_;
	friend ptr<void> malloc(size_t);
	friend void free();
	friend ptr<void> memset(ptr<void> dest, int ch, std::size_t byte_count);
	template<class TT, class RRawPtr> friend struct managed::ptr;
private:
//	ptr(ptr<void const> const& p) : rp_{const_cast<void*>(p.rp_)}{}
	template<class TT> friend ptr<TT> const_pointer_cast(ptr<TT const> const&);
	template<class, class> friend struct ptr;
	ptr(raw_pointer rp) : rp_{rp}{}
	operator raw_pointer() const{return rp_;}
	friend ptr<void> malloc(std::size_t);
	friend void free(ptr<void>);
public:
	ptr() = default;
	ptr(ptr const& other) : rp_{other.rp_}{}//= default;
	ptr(std::nullptr_t n) : rp_{n}{}
	template<class Other, typename = decltype(raw_pointer{std::declval<Other const&>().rp_})>
	ptr(Other const& o) : rp_{o.rp_}{}
	ptr& operator=(ptr const&) = default;
	bool operator==(ptr const& other) const{return rp_==other.rp_;}
	bool operator!=(ptr const& other) const{return rp_!=other.rp_;}

	using pointer = ptr<T>;
	using element_type    = typename std::pointer_traits<raw_pointer>::element_type;
	using difference_type = typename std::pointer_traits<raw_pointer>::difference_type;
	template<class U> using rebind = ptr<U, typename std::pointer_traits<raw_pointer>::template rebind<U>>;

	explicit operator bool() const{return rp_;}
//	explicit operator raw_pointer&()&{return impl_;}
	friend ptr to_address(ptr const& p){return p;}
};

template<typename T, typename RawPtr>
struct ptr{
	using raw_pointer = RawPtr;
protected:
	raw_pointer rp_;
	using raw_pointer_traits = typename std::pointer_traits<raw_pointer>;
	template<class TT> friend class allocator;
	using default_allocator_type = typename cuda::allocator<T>;
	template<typename, typename> friend struct ptr;
	template<typename> friend struct ref;

//	template<class TT, typename = typename std::enable_if<not std::is_const<TT>{}>::type> 
//	ptr(ptr<TT const> const& p) : rp_{const_cast<T*>(p.rp_)}{}
	template<class TT> friend ptr<TT> const_pointer_cast(ptr<TT const> const&);
	friend struct managed::ptr<T, RawPtr>;
public:
	template<class U> using rebind = ptr<U, typename std::pointer_traits<raw_pointer>::template rebind<U>>;

	template<class Other, typename = std::enable_if_t<std::is_convertible<std::decay_t<decltype(std::declval<ptr<Other>>().rp_)>, raw_pointer>{} and not std::is_same<Other, T>{} >>
	/*explicit(false)*/ constexpr ptr(ptr<Other> const& o) : rp_{static_cast<raw_pointer>(o.rp_)}{}
	template<class Other, typename = std::enable_if_t<not std::is_convertible<std::decay_t<decltype(std::declval<ptr<Other>>().rp_)>, raw_pointer>{} and not std::is_same<Other, T>{}>, typename = decltype(static_cast<raw_pointer>(std::declval<ptr<Other>>().rp_))>
	explicit/*(true)*/ constexpr ptr(ptr<Other> const& o, void** = 0) : rp_{static_cast<raw_pointer>(o.rp_)}{}
	explicit constexpr ptr(raw_pointer rp)  : rp_{rp}{}
	template<class Other, typename = decltype(static_cast<raw_pointer>(std::declval<Other const&>().rp_))> 
	explicit ptr(Other const& o) : rp_{static_cast<raw_pointer>(o.rp_)}{}
	ptr() = default;
	ptr(ptr const&) = default;
	ptr(std::nullptr_t nu) : rp_{nu}{}
	ptr& operator=(ptr const&) = default;
	constexpr bool operator==(ptr const& other) const{return rp_==other.rp_;}
	constexpr bool operator!=(ptr const& other) const{return rp_!=other.rp_;}
	template<class Other>
	auto operator==(ptr<Other> const& other) const
	->decltype(rp_==other.rp_){
		return rp_==other.rp_;}
	template<class Other>
	auto operator!=(ptr<Other> const& other) const
	->decltype(rp_!=other.rp_){
		return rp_!=other.rp_;}
	using element_type    = typename raw_pointer_traits::element_type;
	using difference_type = typename raw_pointer_traits::difference_type;
	using size_type       = difference_type;
	using value_type      = T;

	using pointer = ptr<T, RawPtr>;//<T>;
	using iterator_category = typename std::iterator_traits<raw_pointer>::iterator_category;
	explicit operator bool() const HD{return rp_;}
	using void_C_type = typename std::conditional<std::is_const<typename std::pointer_traits<RawPtr>::element_type>{}, void const, void>::type;
	explicit operator typename raw_pointer_traits::template rebind<void_C_type>() const HD{return {rp_};}
	ptr& operator++(){++rp_; return *this;}
	ptr& operator--(){--rp_; return *this;}
	ptr  operator++(int){auto tmp = *this; ++(*this); return tmp;}
	ptr  operator--(int){auto tmp = *this; --(*this); return tmp;}
	ptr& operator+=(typename ptr::difference_type n) HD{rp_+=n; return *this;}
	ptr& operator-=(typename ptr::difference_type n) HD{rp_-=n; return *this;}
//	friend bool operator==(ptr const& s, ptr const& t){return s.impl_==t.impl_;}
//	friend bool operator!=(ptr const& s, ptr const& t){return s.impl_!=t.impl_;}
	constexpr ptr operator+(typename ptr::difference_type n) const {return ptr{rp_ + n};}
	constexpr ptr operator-(typename ptr::difference_type n) const HD{return ptr{rp_ - n};}
	using reference = ref<element_type>;
//#ifdef __NVCC__
//	#ifndef __CUDA_ARCH__
//		__host__   constexpr reference operator*() const{return {*this};}
//	#else
//		__device__ constexpr reference operator*() const{return *rp_; }
//	#endif
//#else
	constexpr reference operator*() const __host__ __device__ { return {*this}; }
//  __device__ reference operator*() const{return *rp_;}
//#endif
	reference operator[](difference_type n) const __host__ __device__{return *((*this)+n);}
	friend ptr to_address(ptr const& p){return p;}
	difference_type operator-(ptr const& o) const HD{return rp_-o.rp_;}
	operator ptr<void>(){return {rp_};}
	auto get() const{return rp_;}
//	#ifdef __CUDA_ARCH__
	explicit operator raw_pointer() const HD{return rp_;}
//	#else
//	explicit operator raw_pointer() const HD{return rp_;}
//	#endif
	raw_pointer raw_pointer_cast() const HD{return this->rp_;}
	friend raw_pointer raw_pointer_cast(ptr const& self) HD{return self.rp_;}
	template<class PM>
	HD auto operator->*(PM&& pm) const
	->decltype(ref<std::decay_t<decltype(rp_->*std::forward<PM>(pm))>>{ptr<std::decay_t<decltype(rp_->*std::forward<PM>(pm))>>{&(rp_->*std::forward<PM>(pm))}}){
		return ref<std::decay_t<decltype(rp_->*std::forward<PM>(pm))>>{ptr<std::decay_t<decltype(rp_->*std::forward<PM>(pm))>>{&(rp_->*std::forward<PM>(pm))}};}
public:
	friend allocator<std::decay_t<T>> get_allocator(ptr const&){return {};}
	friend allocator<std::decay_t<T>> default_allocator_of(ptr const&){return {};}
};

template<class T> allocator<T> get_allocator(ptr<T> const&){return {};}


template<
	class Alloc, class InputIt, class Size, class... T, class ForwardIt = ptr<T...>,
	typename InputV = typename std::pointer_traits<InputIt>::element_type, 
	typename ForwardV = typename std::pointer_traits<ForwardIt>::element_type
//	, typename = std::enable_if_t<std::is_constructible<ForwardV, InputV>{}>
>
ForwardIt uninitialized_copy_n(InputIt f, Size n, ptr<T...> d){
	if(std::is_trivially_constructible<ForwardV, InputV>{})
		return memcpy(d, f, n*sizeof(ForwardV)) + n;
	else assert(0);
	return d;
}

template<
	class Alloc, class InputIt, class Size, class... T, class ForwardIt = ptr<T...>,
	typename InputV = typename std::pointer_traits<InputIt>::element_type, 
	typename ForwardV = typename std::pointer_traits<ForwardIt>::element_type
//	, typename = std::enable_if_t<std::is_constructible<ForwardV, InputV>{}>
>
ForwardIt alloc_uninitialized_copy_n(Alloc&, InputIt f, Size n, ptr<T...> d){
	if(std::is_trivially_constructible<ForwardV, InputV>{})
		return memcpy(d, f, n*sizeof(ForwardV)) + n;
	else assert(0);
	return d;
}

template<class Alloc, class InputIt, typename Size, class... T, class ForwardIt = ptr<T...>>
ForwardIt alloc_uninitialized_move_n(Alloc& a, InputIt f, Size n, ptr<T...> d){
	return alloc_uninitialized_copy_n(a, f, n, d);
}

template<class T> 
ptr<T> const_pointer_cast(ptr<T const> const& p){return ptr<T>{p.impl_};}

template<class TTT>
static std::true_type is_ref_aux(ref<TTT> const&);
std::false_type is_ref_aux(...);

template<class TTT> struct is_ref : decltype(is_ref_aux(std::declval<TTT>())){};

template<class To, class From, std::enable_if_t<std::is_convertible<From, To>{},int> =0>
constexpr To implicit_cast(From&& f){return static_cast<To>(f);}

template<class T>
struct ref{
	using value_type = T;
	using reference = value_type&;
	using pointer = ptr<T>;
	using raw_reference = value_type&;
private:
	pointer pimpl_;
	ref(pointer const& p) HD: pimpl_{p}{}
	template<class TT> friend struct ref;
public:
	constexpr ref(T& t) : pimpl_{&t}{}
//	ref(T& t) HD : pimpl_{&t}{}
	template<class Other, typename = decltype(implicit_cast<pointer>(std::declval<ref<Other>>().pimpl_))>
	/*explicit(false)*/ ref(ref<Other>&& o) HD : pimpl_{implicit_cast<pointer>(std::move(o).pimpl_)}{}
	template<class Other, typename = std::enable_if_t<not std::is_convertible<std::decay_t<decltype(std::declval<ptr<Other>>())>, pointer>{}>>
	explicit/*(true)*/ ref(ref<Other> const& o, void** = 0) HD : pimpl_{static_cast<pointer>(o)}{}
	template<class TT, class PP> friend struct ptr;
//	typename pointer::raw_pointer operator&() & __device__{return pimpl_.rp_;}
//	typename pointer::raw_pointer operator&() const& __device__{return pimpl_.rp_;}
//	typename pointer::raw_pointer operator&() && __device__{return pimpl_.rp_;}

	pointer operator&() & __host__ __device__{return pimpl_;}
	pointer operator&() const& __host__ __device__{return pimpl_;}
	pointer operator&() && __host__ __device__{return pimpl_;}

	struct skeleton_t{
		char buff[sizeof(T)]; T* p_;
		[[SLOW]] 
		skeleton_t(T* p) HD : p_{p}{
			#if __CUDA_ARCH__
			#else
//			[[maybe_unused]] 
			cudaError_t s = cudaMemcpy(buff, p_, sizeof(T), cudaMemcpyDeviceToHost); 
			(void)s; assert(s == cudaSuccess);
			#endif	
		}
		operator T&()&& HD{return reinterpret_cast<T&>(buff);}
		void conditional_copyback_if_not(std::false_type) const HD{
			#if __CUDA_ARCH__
		//	*p_ = reinterpret_cast<T const&>(
			#else
		//	[[maybe_unused]] 
			cudaError_t s = cudaMemcpy(p_, buff, sizeof(T), cudaMemcpyHostToDevice); 
			(void)s; assert(s == cudaSuccess);
			#endif
		}
		void conditional_copyback_if_not(std::true_type) const HD{
			#if __CUDA_ARCH__
		//	*p_ = reinterpret_cast<T const&>(
			#else
		//	[[maybe_unused]] 
			cudaError_t s = cudaMemcpy(p_, buff, sizeof(T), cudaMemcpyHostToDevice); 
			(void)s; assert(s == cudaSuccess);
			#endif
		}
		~skeleton_t() HD{conditional_copyback_if_not(std::is_const<T>{});}
	};
	skeleton_t skeleton()&& HD{return {pimpl_.rp_};}
public:
	constexpr ref(ref&& r) : pimpl_{std::move(r.pimpl_).rp_}{}
//	ref& operator=(ref const&)& = delete;
private:
	ref& move_assign(ref&& other, std::true_type)&{
		cudaError_t s = cudaMemcpy(pimpl_.rp_, other.rp_, sizeof(T), cudaMemcpyDeviceToDevice); (void)s; assert(s == cudaSuccess);
		return *this;
	}
	ref& move_assign(ref&& other, std::false_type)&{
		cudaError_t s = cudaMemcpy(pimpl_.rp_, other.rp_, sizeof(T), cudaMemcpyDeviceToDevice); (void)s; assert(s == cudaSuccess);
		return *this;
	}
public:
#if __CUDA__
#ifdef __NVCC__
  #ifndef __CUDA_ARCH__
	template<class TT>
	[[deprecated]]
    __host__ auto operator=(TT&& t) &&
	->decltype(*pimpl_.rp_ = std::forward<TT>(t), std::move(*this)){
		assert(0); return std::move(*this);}
  #else
	template<class TT>
    __device__ auto operator=(TT&& t) &&
	->decltype(*pimpl_.rp_ = std::forward<TT>(t), std::move(*this)){
		return *pimpl_.rp_ = std::forward<TT>(t), std::move(*this);}
  #endif
#else
	template<class TT>
	[[deprecated("because it implies slow memory access, suround code with CUDA_SLOW")]]
	__host__ auto operator=(TT&& t) && 
	->decltype(*pimpl_.rp_ = std::forward<TT>(t), std::move(*this)){	//	assert(0);
		static_assert(std::is_trivially_assignable<T&, TT&&>{}, "!");
		cudaError_t s=cudaMemcpy(pimpl_.rp_, std::addressof(t), sizeof(T), cudaMemcpyHostToDevice);assert(s==cudaSuccess);(void)s;
		return std::move(*this);
	}
	template<class TT>
	__device__ ref&& operator=(TT&& t) &&{*pimpl_.rp_ = std::forward<TT>(t); return std::move(*this);}
#endif
#else
	template<class TT>
	[[deprecated("because it implies slow memory access, suround code with CUDA_SLOW")]]
	auto operator=(TT&& t) && 
	->decltype(*pimpl_.rp_ = std::forward<TT>(t), std::move(*this)){	//	assert(0);
		static_assert(std::is_trivially_assignable<T&, TT&&>{}, "!");
		cudaError_t s=cudaMemcpy(pimpl_.rp_, std::addressof(t), sizeof(T), cudaMemcpyHostToDevice);assert(s==cudaSuccess);(void)s;
		return std::move(*this);
	}	
#endif

#if 0
#if defined(__clang__)
	decltype(auto) operator=(ref const& other) && __device__ {return operator=(static_cast<T const&>(other));}
	decltype(auto) operator=(ref&  other) && __device__ {return operator=(static_cast<T&>(other));}
//	decltype(auto) operator=(ref&& other) &  __device__{return operator=(static_cast<T const&>(std::move(other)));}
//	decltype(auto) operator=(ref&& other) && __device__{return operator=(static_cast<T const&>(std::move(other)));}
#endif
	ref&& operator=(ref&& other) && __host__{
		static_assert( std::is_trivially_copyable<value_type>{}, "!");
		auto s=cudaMemcpy(pimpl_.rp_, other.pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToDevice); (void)s; assert(s==cudaSuccess);
		return std::move(*this);
	}
#if not defined(__clang__)
	[[deprecated("WARNING: slow memory operation")]]
	ref&& operator=(value_type const& t) && HD {
		#ifdef __CUDA_ARCH__
			*(pimpl_.rp_) = t;
		//	assert(0);
		#else
		if(std::is_trivially_copy_assignable<T>{}){
			/*[[maybe_unused]]*/ cudaError_t s= cudaMemcpy(pimpl_.rp_, std::addressof(t), sizeof(T), cudaMemcpyHostToDevice);
		//	assert(s == cudaSuccess); (void)s;
			if( s != cudaSuccess ) throw std::runtime_error( cudaGetErrorString(s) );
		}else{
			char buff[sizeof(T)];
			/*[[maybe_unused]]*/ cudaError_t s1 = cudaMemcpy(buff, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost); 
			assert(s1 == cudaSuccess); (void)s1;
			reinterpret_cast<T&>(buff) = t;
			/*[[maybe_unused]]*/ cudaError_t s2 = cudaMemcpy(pimpl_.rp_, buff, sizeof(T), cudaMemcpyHostToDevice); 
			assert(s2 == cudaSuccess); (void)s2;
		}
		#endif
		return std::move(*this);
	}
	#ifndef __CUDA_ARCH__
	[[deprecated("WARNING: slow memory operation")]]
	#else
	#endif
	decltype(auto) operator=(value_type const& t) & HD{
		#pragma GCC diagnostic push
		#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
		return std::move(std::move(*this) = t);
		#pragma GCC diagnostic pop
	}
#else // this is clang
	template<class ValueType, 
		std::enable_if_t<std::is_assignable<T&, decltype(value_type{std::declval<ValueType>()})>{}, int> = 0
	>
	[[deprecated("WARNING: slow cuda memory operation")]]
	ref&& operator=(ValueType const& t) && __host__ {
		static_assert( std::is_trivially_copy_assignable<T>{}, "!" );
	//	if(std::is_trivially_copy_assignable<T>{}){
		//	value_type const& tt = t;
			cudaError_t s= cudaMemcpy(pimpl_.rp_, std::addressof(t), sizeof(T), cudaMemcpyHostToDevice);
		//	assert(s == cudaSuccess); (void)s;
			if( s != cudaSuccess ) throw std::runtime_error( cudaGetErrorString(s) );
	//	}else{
	//		char buff[sizeof(T)];
	//		/*[[maybe_unused]]*/ cudaError_t s1 = cudaMemcpy(buff, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost); 
	//		assert(s1 == cudaSuccess); (void)s1;
	//		reinterpret_cast<std::decay_t<T>&>(buff) = t;
	//		/*[[maybe_unused]]*/ cudaError_t s2 = cudaMemcpy(pimpl_.rp_, buff, sizeof(T), cudaMemcpyHostToDevice); 
	//		assert(s2 == cudaSuccess); (void)s2;
	//	}
		return std::move(*this);
	}
	[[deprecated("WARNING: slow memory operation")]]
	decltype(auto) operator=(value_type const& t) & __host__{
		#pragma clang diagnostic push
		#pragma clang diagnostic ignored "-Wdeprecated-declarations"
		return std::move(std::move(*this) = t);
		#pragma clang diagnostic pop
	}
	#if defined(__CUDA__)
	ref&& operator=(value_type const& t) && __device__ {
		*(pimpl_.rp_) = t;
		return std::move(*this);
	}
	ref& operator=(value_type const& t) & __device__ {
		*(pimpl_.rp_) = t;
		return *this;
	}
	#endif
#endif
#endif

#if defined(__clang__)
#if defined(__CUDA__) //&& !defined(__CUDA_ARCH__)
	operator T()&& __device__{return *(pimpl_.rp_);}
	operator T()&& __host__  {static_assert( std::is_trivially_copyable<std::decay_t<T>>{}, "!" );
		typename std::aligned_storage<sizeof(T), alignof(T)>::type ret;
		{cudaError_t s=cudaMemcpy((void*)&ret, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost); assert(s == cudaSuccess); (void)s;}
		return *reinterpret_cast<T*>(&ret);
	}
#else
	[[SLOW]] operator T()&&{
		char buff[sizeof(T)];
		cudaError_t s = cudaMemcpy(buff, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost);
		switch(s){
			case cudaSuccess: break;
			case cudaErrorInvalidValue: throw std::runtime_error{"cudaErrorInvalidValue"};
			case cudaErrorInvalidMemcpyDirection: throw std::runtime_error{"cudaErrorInvalidMemcpyDirection"};
			default: throw std::runtime_error{"unknown error"};
		}
		return std::move(reinterpret_cast<T&>(buff));
	}
#endif
#else // no clang
#if __CUDA_ARCH__
	operator T()&& __device__{return *(pimpl_.rp_);}
#else
	[[SLOW]] operator T()&& __host__{
		char buff[sizeof(T)];
		{cudaError_t s = cudaMemcpy(buff, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost); assert(s == cudaSuccess); (void)s;}
		return std::move(reinterpret_cast<T&>(buff));
	}
#endif
#if defined(__clang__)
	[[SLOW]] operator T() const& __host__{
		char buff[sizeof(T)];
		{
		//	cudaError_t s = cudaMemcpy(buff, this->rp_, sizeof(T), cudaMemcpyDeviceToHost);
			auto e = static_cast<Cuda::error>(cudaMemcpy(buff, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost));
			if(e != Cuda::error::success) throw std::system_error(e, " when trying to memcpy for element access");
		}
		return std::move(reinterpret_cast<T&>(buff));
	}
	operator T() const& __device__{return *(pimpl_.rp_);}
#else //no clang
#if __CUDA_ARCH__
	operator T() const& __device__{return *(pimpl_.rp_);}
#else
	[[SLOW]] operator T() const& __host__{
		char buff[sizeof(T)];
		{
			auto e = static_cast<Cuda::error>(cudaMemcpy(buff, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost));
			if(e != Cuda::error::success) throw std::system_error(e, " when trying to memcpy for element access");
		}
		return std::move(reinterpret_cast<T&>(buff));
	}
#endif
#endif
	#endif







#ifndef _MULTI_MEMORY_CUDA_DISABLE_ELEMENT_ACCESS
	bool operator!=(ref const& other) const&{return not(*this == other);}
	template<class Other>
	bool operator!=(ref<Other>&& other)&&{
		char buff1[sizeof(T)];
		/*[[maybe_unused]]*/ cudaError_t s1 = cudaMemcpy(buff1, this->impl_, sizeof(T), cudaMemcpyDeviceToHost); assert(s1 == cudaSuccess); (void)s1;
		char buff2[sizeof(Other)];
		/*[[maybe_unused]]*/ cudaError_t s2 = cudaMemcpy(buff2, other.impl_, sizeof(Other), cudaMemcpyDeviceToHost); assert(s2 == cudaSuccess); (void)s2;
		return reinterpret_cast<T const&>(buff1)!=reinterpret_cast<Other const&>(buff2);
	}
#else
//	bool operator==(ref const& other) const = delete;
#endif
#if 1

#if 0
	template<class Other> 
	[[deprecated("WARNING: slow memory operation")]]
	auto operator==(Other const& other)&&
#if __CUDA_ARCH__
	->decltype(*(pimpl_.rp_)==other){
		return *(pimpl_.rp_)==other;}
#else
	->decltype(static_cast<T const&>(std::move(*this))==other){
		return static_cast<T const&>(std::move(*this))==other;}
#endif
#endif

#if defined(__clang__)
#if defined(__CUDA__) && defined(__CUDA_ARCH__)
	template<class Other, typename = std::enable_if_t<not is_ref<std::decay_t<Other>>{}> > 
	friend auto operator==(ref&& self, Other&& other) __host__{
//#if __CUDA_ARCH__
//		return std::forward<Other>(other)==*(this->rp_);
//		return *(self->rp_) == std::forward<Other>(other);
//#else
		return std::move(self).operator T() == std::forward<Other>(other);
	//	return static_cast<T>(std::move(self)) == std::forward<Other>(other);
//#endif
	}
	template<class Other, typename = std::enable_if_t<not is_ref<Other>{}> > 
	friend auto operator==(ref&& self, Other&& other) __device__{
		return *(self->rp_) == std::forward<Other>(other);
	}
#else
	template<class Other, typename = std::enable_if_t<not is_ref<Other>{}> > 
	friend auto operator==(ref&& self, Other&& other) __host__{
		return std::move(self).operator T() == std::forward<Other>(other);
	}
#endif
#else // no clang
	template<class Other, typename = std::enable_if_t<not is_ref<Other>{}> > 
	friend auto operator==(ref&& self, Other&& other) HD{
//	#if __CUDA_ARCH__
//		return *(self.pimpl_.rp_) == std::forward<Other>(other);
//	#else
		return static_cast<T>(std::move(self)) == std::forward<Other>(other);
//	#endif
	}
#endif

	friend decltype(auto) raw_reference_cast(ref&& r){return *raw_pointer_cast(&r);}
	friend auto raw_value_cast(ref&& r){return std::move(r).operator T();}
	auto raw_value_cast()&&{return std::move(*this).operator T();}

	template<class Other, typename = std::enable_if_t<not is_ref<Other>{}> > 
	friend auto operator==(Other&& other, ref&& self){
#if __CUDA_ARCH__
//		return std::forward<Other>(other)==*(this->rp_);
		return std::forward<Other>(other)==*(self->rp_);
#else
		return std::forward<Other>(other)==static_cast<T>(std::move(self));
#endif
	}
	template<class Other, typename = std::enable_if_t<not std::is_same<T, Other>{}> >
	[[SLOW]]
	bool operator==(ref<Other>&& other)&&{
//#pragma message ("Warning goes here")
		char buff1[sizeof(T)];
	//	cuda::memcpy(buff1, ref::rp_, sizeof(T));
		/*[[maybe_unused]]*/ cudaError_t s1 = cudaMemcpy(buff1, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost);
		assert(s1 == cudaSuccess); (void)s1;
		char buff2[sizeof(Other)];
		/*[[maybe_unused]]*/ cudaError_t s2 = cudaMemcpy(buff2, raw_pointer_cast(&other), sizeof(Other), cudaMemcpyDeviceToHost); 
		assert(s2 == cudaSuccess); (void)s2;
		return reinterpret_cast<T const&>(buff1)==reinterpret_cast<Other const&>(buff2);
	}
#if 1
	[[SLOW]] bool operator==(ref const& other) &&{
		char buff1[sizeof(T)];
		{/*[[maybe_unused]]*/ cudaError_t s1 = cudaMemcpy(buff1, pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost); assert(s1 == cudaSuccess); (void)s1;}
		char buff2[sizeof(T)];
		{/*[[maybe_unused]]*/ cudaError_t s2 = cudaMemcpy(buff2, other.pimpl_.rp_, sizeof(T), cudaMemcpyDeviceToHost); assert(s2 == cudaSuccess); (void)s2;}
		return reinterpret_cast<T const&>(buff1)==reinterpret_cast<T const&>(buff2);
	}
#endif
#endif
//	[[SLOW]]
//	operator T const&()&& HD{return *(this->rp_);}
//	operator T&&()&& HD{return std::move(*(this->rp_));}
//	operator T const&() const& HD{return *(this->rp_);}
//	operator T&()& HD{return *(this->rp_);}
//	#else

	template<class Other, typename = decltype(std::declval<T&>()+=std::declval<Other&&>())>
	__host__ __device__
	ref& operator+=(Other&& o)&&{std::move(*this).skeleton()+=o; return *this;}
	template<class Other, typename = decltype(std::declval<T&>()-=std::declval<Other&&>())>
	ref&& operator-=(Other&& o)&&{std::move(*this).skeleton()-=o; return std::move(*this);}
private:
	template<class Ref>
	void swap(Ref&& b) &&{
		T tmp = std::move(*this);
	BEGIN_CUDA_SLOW
		std::move(*this) = std::forward<Ref>(b);
		std::forward<Ref>(b) = std::move(tmp);
	END_CUDA_SLOW
	}
public:
#ifdef __NVCC__
#define DEPRECATED(MsG)	__attribute__((deprecated))
#else
#define	DEPRECATED(MsG) [[deprecated(MsG)]]
#endif

	template<class Ref>
#if __NVCC__
	__attribute__((deprecated))
#else
	[[deprecated("WARNING: slow cuda memory operation")]]
#endif
	friend void swap(ref&& a, Ref&& b){a.swap(std::forward<Ref>(b));}
	template<class Ref> DEPRECATED("WARNING: slow cuda memory operation")
	friend void swap(Ref&& a, ref&& b){std::move(b).swap(a);}
	DEPRECATED("WARNING: slow cuda memory operation")
	friend void swap(ref&& a, ref&& b){std::move(a).swap(std::move(b));}
	ref<T>&& operator++()&&{++(std::move(*this).skeleton()); return std::move(*this);}
	ref<T>&& operator--()&&{--(std::move(*this).skeleton()); return std::move(*this);}
	template<class Self, typename = std::enable_if_t<std::is_base_of<ref, Self>{}>>
	friend auto conj(Self&& self, ref* = 0){return conj(std::forward<Self>(self).skeleton());}
};

}}}}

namespace thrust{
template<class T, class P> P raw_pointer_cast(boost::multi::memory::cuda::ptr<T, P> const& p) __host__ __device__{
	return p.raw_pointer_cast();
}
}
#undef SLOW

#ifdef _TEST_MULTI_MEMORY_ADAPTORS_CUDA_PTR

#define BOOST_TEST_MODULE "C++ Unit Tests for Multi CUDA allocators"
#define BOOST_TEST_DYN_LINK
#include<boost/test/unit_test.hpp>

#include "../cuda/malloc.hpp"

namespace multi = boost::multi;
namespace cuda = multi::memory::cuda;

template<class T> __device__ void WHAT(T&&) = delete;

#if __CUDA_ARCH__
__device__ void f(cuda::ptr<double> p){
//	printf("%f", *p);
	printf("%f", static_cast<double const&>(*p));
}
#endif

BOOST_AUTO_TEST_CASE(multi_memory_cuda_ptr){

//	static_assert( not std::is_convertible<std::complex<double>*, multi::memory::cuda::ptr<std::complex<double>>>{}, "!" );
//	static_assert( not std::is_convertible<multi::memory::cuda::ptr<std::complex<double>>, std::complex<double>*>{}, "!" );

	multi::memory::cuda::ptr<std::complex<double>> xxx = nullptr;
	std::complex<double>* ppp = xxx;

	using T = double; 
	static_assert( sizeof(cuda::ptr<T>) == sizeof(T*), "!");
	std::size_t const n = 100;
	{
		using cuda::ptr;
		auto p = static_cast<ptr<T>>(cuda::malloc(n*sizeof(T)));
		CUDA_SLOW( *p = 99. );
		{
			ptr<T const> pc = p;
			BOOST_REQUIRE( *p == *pc );
		}
		BOOST_REQUIRE( CUDA_SLOW( *p == 99. ) );
		BOOST_REQUIRE( *p != 11. );
		cuda::free(p);
		cuda::ptr<T> P = nullptr; (void)P;
		ptr<void> pv = p; (void)pv;

	}
//	what<typename cuda::ptr<T>::rebind<T const>>();
//	what<typename std::pointer_traits<cuda::ptr<T>>::rebind<T const>>();
	static_assert( std::is_same<typename std::pointer_traits<cuda::ptr<T>>::rebind<T const>, cuda::ptr<T const>>{} , "!");	
}

BOOST_AUTO_TEST_CASE(ptr_conversion){
	cuda::ptr<double> p = nullptr;
	cuda::ptr<double const> pc = p;
}

template<class T> struct Complex_{T real; T imag;};

BOOST_AUTO_TEST_CASE(multi_memory_cuda_ptr_member_pointer){
	
	Complex_<double> c{10.,20.};
//	double Complex_<double>::* 
	Complex_<double>* p = &c;
	auto pm = &Complex_<double>::imag;
	BOOST_REQUIRE( p->*pm == 20. );
	BOOST_REQUIRE( *p.*pm == 20. );

//	cuda::ptr<Complex_<double>> pcu;
//	pcu->*pm;
}



#endif
#endif

